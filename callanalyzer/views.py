from django.shortcuts import render,get_object_or_404
from .models import call
# from .form import callForm
import random
# Create your views here.

# def index(request):
#     html_ = """
#     <!DOCTYPE html>
#     <html lang="en" dir="ltr">
#       <head>
#         <meta charset="utf-8">
#         <title>Call Analyzer</title>
#       </head>
#       <body>
#         Hi There!
#       </body>
#     </html>
#     """
#     return HttpResponse(html_)

def index(request):
    file = call.objects
    return render(request,"base.html",{'form':file})
