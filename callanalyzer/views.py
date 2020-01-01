from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    html_ = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Call Analyzer</title>
      </head>
      <body>
        Hi There!
      </body>
    </html>
    """
    return HttpResponse(html_)
