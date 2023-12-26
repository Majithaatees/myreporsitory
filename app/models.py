from django.db import models

# Create your models here.
class customer(models.Model):
    fname=models.CharField(max_length=250)
    lname=models.CharField(max_length=250)
    age=models.IntegerField()
class student(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirmpassword=models.CharField(max_length=200)
    phone=models.IntegerField()
