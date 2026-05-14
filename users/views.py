from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.contrib.auth import login

def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            UserProfile.objects.create(user=new_user)
            login(request,new_user)
            return redirect('home_page:home')
    
    context = {'form':form}
    return render(request,'SignUp.html',context)





