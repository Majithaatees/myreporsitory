from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import customer, student


# Create your views here.
def home(request):
    if 'username' in request.session:
        current_user=request.session['username']
        uname=student.objects.get(username=current_user)
        return render(request,'home.html',{'current_user':current_user,"uname":uname})
    return render(request,"home.html")
def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['passw']
        cpass=request.POST['cpass']
        phno=request.POST['phno']
        if pwd==cpass:
            student(username=uname,password=pwd,confirmpassword=cpass,phone=phno).save()
            return render(request,"login.html")
        else:
            messages.error(request,"Password does not match")
            return render(request,"reg.html")
    return render(request,"reg.html")
def contact(request):
    return render(request,"contact.html")
def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pas=request.POST['passwd']
        customerd=student.objects.filter(username=uname,password=pas)
        if customerd:
            request.session['username']=uname
            return redirect('home')
        else:
            messages.error(request,"Password and username does not match")
    return render(request,"login.html")
def logout(request):
    del request.session['username']
    return redirect('home')
def senemail(request):
    if request.method=='POST':
        emailid=request.POST['email']
        message=request.POST['message']
        send_mail()
    return render(request,"email.html")
