from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from home.models import Student,Teacher
from django.contrib.auth import logout,authenticate,login
from django.core.mail import EmailMessage
from django.urls import resolve

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
    'Login Notification',
    'We found a new login',
    'portaltoportal@123',
    [email,'nonu592002@gmail.com'],
    # reply_to=['another@example.com'],
    # headers={'Message-ID': 'foo'},
    )
    email.send()
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

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    user = request.user
    name = user.username
    studnets = Student.objects.all()
    for std in studnets:
        if std.user.username == name:
            break
    rollno = std.rollno
    phone = std.phone
    useremail = user.email
    fullname =  request.user.get_full_name()
    context = {'username' : name,'rollno' : rollno,'email' : useremail,
                'phone':phone,'fname':std.fName,'branch':std.branch,
                'year' : std.year,'city':std.city,'dob':std.dob,'fullname':fullname    
            }
    return render(request,'index.html',context)

def course(request):
    if request.user.is_anonymous:
        return redirect('/login')
    current_url = resolve(request.path_info).url_name
    tachers = Teacher.objects.all
    # for t in tachers:
    #     if t.subject == 'maths':
    #       maths = t
    #       elif t.subject == 'physics':
            # phy = y
            # else:
            #     chem = t
    if current_url == 'courseA':
        return render(request,'CourseA.html')
    elif current_url == 'courseB':
        return render(request, 'CourseB.html')
    else :
        return render(request, 'coursec.html')
    
