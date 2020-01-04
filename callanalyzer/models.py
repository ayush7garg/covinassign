from django.db import models
from django import forms
# Create your models here.
class call(models.Model):
    file = models.FileField(upload_to='files/')
    char = models.CharField(max_length=500)
