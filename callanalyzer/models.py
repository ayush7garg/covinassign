from django.db import models

# Create your models here.
class call(models.Model):
    file = models.FileField()
    char = models.CharField(max_length=500)
