from django.shortcuts import render,get_object_or_404
from .models import call
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import FileSerializer

def index(request):
    file = call.objects
    return render(request,"base.html",{'form':file})

class FileView(viewsets.ModelViewSet):
  serializer_class = FileSerializer
  # parser_classes = (MultiPartParser, FormParser)
  # def post(self, request, *args, **kwargs):
  #   file_serializer = FileSerializer(data=request.data)
  #   if file_serializer.is_valid():
  #     file_serializer.save()
  #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
  #   else:
  #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
