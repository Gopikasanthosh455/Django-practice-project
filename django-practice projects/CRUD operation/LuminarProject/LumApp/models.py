from django.db import models

# Create your models here.
class StudentDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Course=models.CharField(max_length=100,null=True,blank=True)
    Mobile_number = models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
class CourseDB(models.Model):
    Course_name=models.CharField(max_length=100,null=True,blank=True)
    Duration=models.CharField(max_length=100,null=True,blank=True)
    Fees=models.IntegerField(null=True,blank=True)
    Institute=models.CharField(max_length=100, null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)