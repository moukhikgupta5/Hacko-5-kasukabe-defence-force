from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h>Welcome to the Home page!</h1>')
def login(request):
    # if request.method == 'POST':
    return HttpResponse('<h>Welcome to the login page!</h1>')
def logout(request):
    return HttpResponse('<h>Welcome to the logout page!</h1>')