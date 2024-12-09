from django.db import models

# Create your models here.
class stud_Db(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Class=models.IntegerField(null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    College=models.CharField(max_length=100,null=True,blank=True)
