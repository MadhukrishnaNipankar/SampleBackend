from django.db import models
from django.contrib.auth.models import User

class BioData(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hobby = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)