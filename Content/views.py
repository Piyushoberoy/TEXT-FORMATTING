from django.shortcuts import redirect, render, HttpResponse,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Data
import os

#CONTENT
def Content(request):
    context={'file':Data.objects.all()}
    if request.user.is_anonymous:
        return redirect("error_404")
    return render(request,'Content/index.html',context)

def nouns(request):
    if request.method=='POST':
        return render(request,'Content/Noun.html')
    return redirect("error_404")

def pronouns(request):
    if request.method=='POST':
        return render(request,'Content/Pronoun.html')
    return redirect("error_404")

def verbs(request):
    if request.method=='POST':
        return render(request,'Content/Verb.html')
    return redirect("error_404")

def adverbs(request):
    if request.method=='POST':
        return render(request,'Content/Adverb.html')
    return redirect("error_404")

def adjectives(request):
    if request.method=='POST':
        return render(request,'Content/Adjective.html')
    return redirect("error_404")

def prepositions(request):
    if request.method=='POST':
        return render(request,'Content/Preposition.html')
    return redirect("error_404")

def conjunctions(request):
    if request.method=='POST':
        return render(request,'Content/Conjunction.html')
    return redirect("error_404")

def interjections(request):
    if request.method=='POST':
        return render(request,'Content/Interjection.html')
    return redirect("error_404")

def articles(request):
    if request.method=='POST':
        return render(request,'Content/Article.html')
    return redirect("error_404")

#SIGN IN/ SIGN UP
'''def login1(request):
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

def register(request):
    return render(request,'Content/registration.html')'''

#USER DATA
'''def handleSignup(request):
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
            print(d)
            return render(request,'Content/registration.html',d)

        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email
        myuser.save()

        messages.success(request,"Your account has been successfully created")
        return redirect("/")
    return redirect("error_404")'''

'''def handlesignin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        d={'username':loginusername}
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home1')
            #return Content(request)
        else:
            messages.error(request,"Invalid credentials, please try again")
            return redirect('home')

    return redirect("error_404")
'''
'''def handlesignout(request):
    logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('home')

def del_user(request):
    print("hello")
    if request.method=='POST':
        print("1258")
        request.user.delete()
        messages.success(request, "Successfully Deleted")
        return HttpResponse("Deleted")
    return redirect("error_404")'''

def Download(request):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type='application/doc')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    return redirect("error_404")
