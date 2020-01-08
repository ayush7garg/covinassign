from rest_framework import serializers
from .models import call
class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = call
    fields = ('file', 'char', 'timestamp')
