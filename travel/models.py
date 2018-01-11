import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Destination(models.Model):

    place = models.CharField(max_length=100)
    date = models.DateTimeField('travel_date')
    info = models.TextField(max_length=1000, default='This is a beautiful place')
    image = models.ImageField(default='None')



    def __str__(self):
        return self.place


class Option(models.Model):

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text






