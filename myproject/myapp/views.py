from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def home(request):
   return render(request,'index.html')

def submit(request):
    return HttpResponse('<b><h1> you submitted data successfully</h1>')