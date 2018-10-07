from django.db import models

# Create your models here.


# 用户
class User(models.Model):
    usertel = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=200)
    useremail = models.CharField(max_length=100)
    usertoken = models.CharField(max_length=200)

class Mei(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    price = models.FloatField()
    flag = models.IntegerField()

    

