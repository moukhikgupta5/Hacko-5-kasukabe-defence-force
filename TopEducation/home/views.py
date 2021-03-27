from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

def home(request):
    user = request.user
    username = user.username
    context = {'username' : username}
    if request.user.is_anonymous:
        return redirect('/login')
    return HttpResponse('<h>Welcome to the Home page!</h1>')
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect('/login')