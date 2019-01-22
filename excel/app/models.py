from django.db import models

# Create your models here.

class ExcelFile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField(blank=False)
    dateIn = models.DateTimeField(blank=False)
    dateOut = models.DateTimeField(blank=False)
    
    numChoices = [(x,x) for x in range(1,34)]
    couriersChoices = (('IP','InPost'),('FED','Fedex'),('PO','Poczta Polska'))
    rs_back = models.IntegerField(choices = numChoices)
    rs =  models.IntegerField(choices = numChoices)
    wood =  models.IntegerField(choices = numChoices)
    eur_s =  models.IntegerField(choices = numChoices)
    eur_ns = models.IntegerField(choices = numChoices)
    couriers = models.CharField(max_length=6, choices=couriersChoices, default='green') 
    
