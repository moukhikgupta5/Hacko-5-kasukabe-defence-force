from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from home.models import Student
from django.contrib.auth import logout,authenticate,login
from django.core.mail import EmailMessage

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    user = request.user
    name = user.username
    studnets = Student.objects.all()
    for std in studnets:
        if std.user.username == name:
            break
    rollno = std.rollno
    useremail = user.email
    emailsubject = "Login on your TopEd Account"
    email = EmailMessage(
    'Hello',
    'Body goes here',
    'moukhikgupta5@google.com',
    ['nonu592002@gmail.com'],
    # reply_to=['another@example.com'],
    # headers={'Message-ID': 'foo'},
    )
    # email.send()
    context = {'username' : name,'rollno' : rollno}
    return render(request,'home.html',context)
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