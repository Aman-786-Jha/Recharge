from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User, auth



# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(max_length=250,blank=False,null=False)
    email = models.EmailField(max_length=300,blank=True)
    subject=models.IntegerField(default=1,blank=True)
    
    message = models.TextField()

    def __str__(self):
        return self.name 
    
    
    

class Recharge(models.Model):
    fk = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    number = models.BigIntegerField()
    rechargeamount = models.IntegerField()
    operator = models.CharField(max_length=100)
    description = models.TextField()
    #complete = models.BooleanField(default=True)

     

class Subscribe(models.Model):
    email =models.EmailField(default='',blank=True)

class CardDetails(models.Model):
    integrity = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(max_length=100,default='',blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100,default='',blank=True)
    state = models.CharField(max_length=100,default='',blank=False,null=False)
    zipcode = models.IntegerField()
    card_on_name = models.CharField(max_length=100,blank=False,null=False)
    creditno = models.TextField()
    expmonth = models.CharField(max_length=14,blank=False,null=False)
    expyear = models.IntegerField()
    cvv = models.IntegerField()

class HeroUnlimited(models.Model):
    talktime = models.TextField()
    data = models.TextField()
    validity = models.IntegerField()
    additional_benefit = models.CharField(max_length=150,blank=True)
    price = models.TextField()

class Recommended(models.Model):
    talktime = models.TextField()
    calls = models.CharField(max_length=20,blank=True,default='NA')
    SMS = models.CharField(max_length=20,blank=True)
    validity = models.TextField()
    additional_benefit = models.CharField(max_length=100,blank=True)
    price = models.TextField()

class OtherPacks(models.Model):
    talktime = models.TextField()
    price = models.TextField()
    




    


