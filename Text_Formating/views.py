from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

def home(request):
    if request.method=="POST":
        logout(request)
        messages.success(request,"Successfully Logged out")
        msg='Successfully Logged out'
        d={'msg':msg}
        return render(request,"Main.html",d)
    return render(request,'Main.html')

'''
def handlesignout(request):
    if request.method=="POST":
        logout(request)
        messages.success(request,"Successfully Logged out")
        msg='Successfully Logged out'
        d={'msg':msg}
        return render(request,"Main.html",d)
    return redirect("error_404")
'''
def home1(request):
    if request.method=='POST':
        loginusername=request.POST.get['loginusername']
        loginpassword=request.POST.get['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        d={'username':loginusername}
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            msg='YOU LOGINED SUCCESFULLY'
            d={'msg':msg}
            return render(request,'OriginalMain.html',d)
        else:
            messages.error(request,"Invalid credentials, type carefully")
            msg='Invalid credentials, type carefully'
            d={'msg':msg}
            return render(request,'Content/login.html',d)
    else:
        return redirect("error_404")

#SIGN IN/ SIGN UP/ ACCOUNT DELETE
def register(request):
    return render(request,'Content/registration.html')

def login1(request):
    return render(request,'Content/login.html')

def frgt_pswd(request):
    return render(request,'Content/frgt_pswd.html')

def frgt_pswd_msg(request):
    if request.method=='POST':
        msg='To reset your password click on reset password or if you have not request for this one then ignore this mail'
        email=request.POST['email']
        send_mail('RESET PASSWORD',
        msg,
        'ynr24genius@gmail.com',
        [email],
        fail_silently=False)
        return render(request,'Content/frgt_pswd_msg.html')
    return redirect("error_404")

def handleSignup(request):
    if request.method=='POST':
        #txt = request.POST.get('text', 'This feature will be available soon.')
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters.")
            msg='Username must be under 10 characters.'
            d={'user_msg':msg}
            return render(request,'registration.html',d)
        if not username.isalnum() :
            messages.error(request,"Username only contains alphabets and numbers.")
            msg='Confirmation Password not matched'
            d={'user_msg':msg}
            return render(request,'registration.html',d)
        if pass1 != pass2:
            messages.error(request,"Confirmation Password not matched")
            #txt = request.POST.get('text', 'This feature will be available soon.')
            msg='Confirmation Password not matched'
            d={'pswd_msg':msg}
            return render(request,'registration.html',d)

        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email
        myuser.save()

        messages.success(request,"Your account has been successfully created")
        msg='Your account has been successfully created'
        d={'msg':msg}
        return render(request,"Main.html",d)
    return redirect("error_404")

def handlesignout(request):
    if request.method=="POST":
        logout(request)
        messages.success(request,"Successfully Logged out")
        msg='Successfully Logged out'
        d={'msg':msg}
        return render(request,"Main.html",d)
    return redirect("error_404")

def del_user(request):
    if request.method=='POST':
        request.user.delete()
        messages.success(request, "Successfully Deleted")
        return HttpResponse("Deleted")
    return redirect("error_404")


def error_404(request):
    return render(request,"Content/404.html")