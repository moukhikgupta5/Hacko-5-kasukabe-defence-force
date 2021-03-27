from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField (max_length=50)
    rollno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=50)
    branch = models.CharField( max_length=50) 
    fName = models.CharField( max_length=50) 
    city = models.CharField( max_length=50) 
    dob = models.DateField()