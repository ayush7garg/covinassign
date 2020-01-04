from django.db import models
# import UploadedFile
# Create your models here.
class call(models.Model):
    file = models.FileField(upload_to='files/')
    char = models.CharField(max_length=999999999999)
    # if InMemoryUploadedFile.multiple_chunks(chunk_size=None):
        # for chunk in InMemoryUploadedFile.chunks(chunk_size=None):
        #     char = char + chunk
    # char = models.CharField(max_length=999999999999)
