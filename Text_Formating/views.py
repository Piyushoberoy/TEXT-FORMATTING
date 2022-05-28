from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
count=0
def home(request):
    global count
    username=""
    msg=""
    users={'username':username,'msg':msg}
    print(count)
    if request.user.is_authenticated:
        users['username']=request.user.username
        users['msg']="Loggined successfully"
    elif count==1:
        users['msg']="Registered successfully"
        count=0
    elif count==101:
        users['msg']="Logout successfully"
        count=0
    elif count<0:
        users['msg']="Account delected successfully"
        count=0
    return render(request, 'OriginalMain.html', users)

#SIGN IN/ SIGN UP/ ACCOUNT DELETE
def register(request):
    return render(request,'Content/registration.html')

def login1(request):
    if request.method=="POST":
        u_name=request.POST.get('loginusername')
        password=request.POST.get('loginpassword')
        user=authenticate(username=u_name, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Logged in successfully!")
            return redirect("/")
        else:
            messages.error(request,"Invalid credentials, type carefully")
            msg='Invalid credentials, type carefully'
            d={'msg':msg}
            return render(request,'Content/login.html',d)

    elif request.user.is_authenticated:
        return redirect("/")
    return render(request, 'Content/login.html')
email=""
def resetemail(request):
    global email
    email=request.POST['email']


def frgt_pswd(request):
    return render(request,'Content/frgt_pswd.html')
    

def frgt_pswd_msg(request):
    global email
    if request.method=='POST':
        resetemail(request)
        if User.objects.filter(email=email):
            user=User.objects.get(email=email)
            msg='Dear,\nYour username is '+user.username+' and to reset your password click on http://127.0.0.1:8000/Password_reset or if you have not request for this one then ignore this mail'
            email=request.POST['email']
            send_mail('RESET PASSWORD',
            msg,
            'ynr24genius@gmail.com',
            [email],
            fail_silently=False)
            return render(request,'Content/frgt_pswd_msg.html')
        return redirect("/Forget_password")
    return redirect("error_404")

def reset_password(request):
    global email
    if request.method=="POST":
        user=User.objects.get(email=email)
        # print(user.first_name)
        password=request.POST.get('password')
        confirmatio_password=request.POST.get('confirmation_password')
        if password==confirmatio_password:
            user.set_password(password)
            user.save()
            email=None
            return redirect('/')
        return redirect("/Password_reset")
    elif request.user.is_authenticated:
        return redirect("/")
    elif email is not None:
        return render(request,"Content/reset_password.html")
    return redirect("/")
def handleSignup(request):
    d=None
    global count
    if request.user.is_authenticated:
        return redirect("/")
    
    elif request.method=="POST":
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
            return render(request,'Content/registration.html',d)
        if not username.isalnum() :
            messages.error(request,"Username only contains alphabets and numbers.")
            msg='Confirmation Password not matched'
            d={'user_msg':msg}
            return render(request,'Content/registration.html',d)
        if pass1 != pass2:
            messages.error(request,"Confirmation Password not matched")
            #txt = request.POST.get('text', 'This feature will be available soon.')
            msg='Confirmation Password not matched'
            d={'pswd_msg':msg}
            return render(request,'Content/registration.html',d)

        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email
        myuser.save()
        count+=1
        messages.success(request, "Account created succesfully!")
        return redirect('/login')
    return render(request, 'Content/registration.html',d)

def handlesignout(request):
    global count
    if request.method=="POST":
        logout(request)
        count=101
        # print(count)
        messages.success(request,"Successfully Logged out")
    return redirect("/")

def del_user(request):
    global count
    if request.method=='POST':
        request.user.delete()
        messages.success(request, "Successfully Deleted")
        count-=1
        return redirect("/")
    return redirect("error_404")


def error_404(request):
    return render(request,"Content/404.html")