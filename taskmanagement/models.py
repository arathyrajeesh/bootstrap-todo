from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    address=models.CharField(max_length=50)
    mobile=models.TextField()
    image=models.ImageField(upload_to='profile_pic/customerprofile_pic/',null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Task(models.Model):
    task_name=models.CharField(max_length=34)
    date=models.DateField()