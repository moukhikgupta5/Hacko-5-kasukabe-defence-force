from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'home.html')
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        username = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return HttpResponse('<h>Welcome to the login page!</h1>')
    return HttpResponse('<h1>Welcome to the login page!</h1>')
def logoutuser(request):
    logout(request)
    return redirect('/login')