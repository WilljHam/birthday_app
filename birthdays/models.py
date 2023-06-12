from django.db import models

# Create your models here.


class Birthday(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
