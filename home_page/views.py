from django.shortcuts import render,redirect
from .models import Service
 
def home(request):
    return render(request,'base.html')

def home_page(request):
    services = Service.objects.all()
    return render(request,'services.html',{'services':services})



