from django.contrib.admin.sites import AlreadyRegistered
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
             if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
             elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
             else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        elif "@gmail.com" or ".edu" or ".org" not in email:
            messages.info(request, "Invalid Email Address")
        else:
            messages.info(request, 'Password Not the Same')
            return redirect('register')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def whatwedo(request):
    return redirect('whatwedo.html')
def goal(request):
    return render(request, 'goal.html')
def high(request):
    return render(request, 'high.html')
def kenyan(request):
    return render(request, 'kenyan.html')
def abroad(request):
    return render(request, 'abroad.html')
