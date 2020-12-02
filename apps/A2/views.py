from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is currently %s.</body></html>" % now
    return HttpResponse(html)