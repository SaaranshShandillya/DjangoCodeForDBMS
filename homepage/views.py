from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
# Create your views here.

def home(request):
        return render(request,'linkinpark.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        num= request.POST["number"]
                
        created_obj = Data.objects.create(name = name, email = email, num=num)
    return render(request,"linkinpark.html")

