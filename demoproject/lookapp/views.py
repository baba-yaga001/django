from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,"welcome.html")

def log(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect(request,'welcome/')
        else:
            messages.info(request,"Invalid username or password")
    return render(request,"log.html")

def reg(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['mail']
        password = request.POST['pass']
        cpwd = request.POST['cpass']

        if password == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exist")
                return redirect("reg")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email exist")
                return redirect("reg")
            else:
                user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email)
                user.save()
                messages.info(request,"User created")
                return redirect(request,'/log')
            # print("Registered")
        else:
            messages.info(request,"Password doesn't match")
            return redirect("reg")
    return render(request,"reg.html")