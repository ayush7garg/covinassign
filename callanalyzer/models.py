from django.db import models
from django import forms
import transpositionEncrypt
# Create your models here.
class call(models.Model):
    file = models.FileField(upload_to='files/')

    char = transpositionEncrypt.encryptMessage(10,file.read())
