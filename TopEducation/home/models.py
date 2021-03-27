from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    rollno = models.CharField(max_length=50)
    phone = models.CharField( max_length=50)
    branch = models.CharField( max_length=50) 
    fName = models.CharField( max_length=50) 
    city = models.CharField( max_length=50) 
    year = models.CharField( max_length=50) 
    dob = models.DateField()
    def __str__(self):
        return self.user.username
class Teacher (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')
    phone = models.CharField( max_length=50) 
    subject = models.CharField( max_length=50)