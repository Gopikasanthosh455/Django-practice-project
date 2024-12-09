from django.db import models

# Create your models here.
class RegisterDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Course=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Mobile=models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
