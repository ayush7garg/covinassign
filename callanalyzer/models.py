from django.db import models
from django import forms
# Create your models here.
class call(models.Model):
    file = models.FileField()
    char = models.CharField(max_length=500)
