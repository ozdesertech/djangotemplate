from django.shortcuts import render
from django.http import HttpResponse
import datetime
def hello(request):
   return render(request, "hello.html")
