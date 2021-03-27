from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from home.models import Student
from django.contrib.auth import logout,authenticate,login

def home(request):
    user = request.user
    username = user.username
    studnets = Student.objects.all()
    
    context = {'username' : username}
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'home.html')
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
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