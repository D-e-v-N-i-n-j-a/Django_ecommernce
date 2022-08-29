from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib import auth as authenticate_user
from .models import Profile
# Create your views here.


def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Credentials does not match')
            return redirect('login') 
        
    return render(request,'login.html')


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password']
        repeat_password = request.POST['repeat_password']
        # IF EMAIL IS NOT PRESENT IN THE DATABASE
        email_is_exist = User.objects.filter(email=email).exists()
        user_name_exist = User.objects.filter(username=username).exists()
        password_does_not_matched = password1 != repeat_password
        if email_is_exist:
            messages.info(request,'email address already taken')
            return redirect('register')
        elif password_does_not_matched:
            messages.info(request,'your password does not match')
            return redirect('register')
        elif user_name_exist:
            messages.info(request,'user name already exist')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,username=username)
            get_user = authenticate_user.get_user(request)
            profile_pic=Profile.objects.create(user = user)
            profile_pic.save()
            user.save()
            print('user created successfully')
            return redirect('login')
        
    return render(request,'register.html') 

# 356626092514845
print('user password connected successfully')


def logout(request):
    auth.logout(request)
    return redirect('/')