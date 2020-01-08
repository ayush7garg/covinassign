from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class call(models.Model):
    file = models.FileField(upload_to='files/', validators=
[FileExtensionValidator(allowed_extensions=['txt'])])
    char = models.CharField(max_length=9999)
