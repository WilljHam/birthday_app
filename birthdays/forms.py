from django import forms
from .models import Birthday



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import calendar


def monthChoices():
    monthchoice = enumerate(calendar.month_name)
    return monthchoice

class BirthdayForm(forms.ModelForm):
    
    
    class Meta:
        model = Birthday
        fields = ['name', 'birthdate']
        widgets = {'birthdate': forms.DateInput(format='%Y-%m-%D', attrs={'type': 'date'}),
                   }



class BirthdaySearchForm(forms.Form):
    name = forms.CharField(max_length=100)

#class BirthdayMonthSearchForm(forms.Form):
#    month = forms.IntegerField()

class BirthdayMonthSearchForm(forms.Form):
    month = forms.ChoiceField(choices=monthChoices())