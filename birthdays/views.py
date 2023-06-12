from django.shortcuts import render, redirect
from django.db.models import F,Q
from django.views.generic.edit import UpdateView

# Create your views here.
from .models import Birthday
import datetime as dt
from .forms import BirthdayForm, BirthdaySearchForm, BirthdayMonthSearchForm
from django.utils import timezone
from datetime import datetime
from django.db.models.functions import Extract


def add_birthday(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('birthday_list')
    else:
        form = BirthdayForm()
    return render(request, 'birthdays/add_birthday.html', {'form': form})


def birthday_list(request):
    today = timezone.now().date()
    next_30_days = today + dt.timedelta(days=30)
    start_date = today
    end_date = next_30_days
    birthdays = Birthday.objects.filter(
    birthdate__month__gte=start_date.month, birthdate__month__lte=end_date.month,)
    birthdays = birthdays.annotate(age=end_date.year-F('birthdate__year'))
    birthdays = birthdays.annotate(month=Extract('birthdate', 'month'),day=Extract('birthdate', 'day')).order_by('month', 'day')

    return render(request, 'birthdays/birthday_list.html', {'birthdays': birthdays})


def search_birthday(request):
    if request.method == 'POST':
        form = BirthdaySearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                birthdays = Birthday.objects.filter(name__icontains=name)
                if len(birthdays)==0:
                    return render(request, 'birthdays/birthday_not_found.html', {'name': name})
                else:
                    birthdays = birthdays.annotate(age=timezone.now().date().year-F('birthdate__year'))
                    return render(request, 'birthdays/birthday_list.html', {'birthdays': birthdays})
            except Birthday.DoesNotExist:
                return render(request, 'birthdays/birthday_not_found.html', {'name': name})
    else:
        form = BirthdaySearchForm()
    return render(request, 'birthdays/search_birthday.html', {'form': form})


def search_month_birthday(request):
    if request.method == 'POST':
        form = BirthdayMonthSearchForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            try:
                birthdays = Birthday.objects.filter(birthdate__month=month)
                if len(birthdays)==0:
                    return render(request, 'birthdays/birthday_month_not_found.html', {'month': month})
                else:
                    birthdays = birthdays.annotate(age=timezone.now().date().year-F('birthdate__year'))
                    return render(request, 'birthdays/birthday_list.html', {'birthdays': birthdays})
            except Birthday.DoesNotExist:
                return render(request, 'birthdays/birthday_month_not_found.html', {'month': month})
    else:
        form = BirthdayMonthSearchForm()
    return render(request, 'birthdays/search_birthday_month.html', {'form': form})

