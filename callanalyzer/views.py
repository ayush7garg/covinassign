from django.shortcuts import render,get_object_or_404
from .models import call
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
    num = random.randint(1,99999999999999)
    some_list = [num,random.randint(1,99999999999999),random.randint(1,99999999999999),random.randint(1,99999999999999)]
    bool_var = True
    context = {
    "name":"Ayush",
    "num":num,
    "some_list":some_list,
    "bool_var":bool_var
    }
    return render(request,'base.html',context)
