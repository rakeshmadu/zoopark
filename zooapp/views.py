from decimal import Decimal
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Registration
from django.contrib.auth import authenticate,login,logout
from .forms import Signupform,Loginform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def Sign(request):
    form = Signupform()
    if request.method =='POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()   
        return redirect(login)
    return render(request,'registration.html',{'form':form})

def login(request):
    form = Loginform()
    if request.method == 'POST':
        form= Loginform(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            log = Registration.objects.filter(email=email,password=password)
            if not log:
                messages.error(request,'username or password not correct')
                return render(request,'login.html')
            else:
                return redirect(home)
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})

def logout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'login.html', context)