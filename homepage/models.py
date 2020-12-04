from django.db import models

class Data(models.Model):
    name=models.CharField(max_length=300)
    email=models.TextField(unique=True)
    num=models.IntegerField()
# Create your models here.