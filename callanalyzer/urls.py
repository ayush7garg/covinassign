from django.urls import path
from django.conf.urls import url

from . import views
from .views import FileView

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
]
