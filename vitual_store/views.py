from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from.models import Store
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from landingpage.models import Products,Reviews

# Create your views here.
@login_required(login_url='/')
def registerStore(request): 
    user = auth.get_user(request) 
    if request.method=='POST':
        store_name = request.POST['store_name']
        email = request.POST['email']
        contact = request.POST['contact']
        location = request.POST['location']
        message = request.POST['description']
        email = Store.objects.filter(email = email).exists()
        check_store_name = Store.objects.filter(store_name=store_name).exists()
        
        if email:
            messages.info(request,'user email already exist please use a different email')
            return redirect('register_store_form')
        
        elif check_store_name:
            messages.info(request,'store name already in use')
            return redirect('register_store_form')
        else:
            store = Store.objects.create(store_name=store_name,email=email,tel=contact,location=location,description=message,is_created = True,user = user)
            store.save()
            
            return redirect('dashboard')
        
            
            
     
    return render(request,'register_store_form.html',{'user':user})



@login_required(login_url='/')
def dashboard(request):
    user = auth.get_user(request)
    
    get_all_products = Products.objects.filter(user = user)
    get_comments = Reviews.objects.filter(user=user).all()
    
    return render(request,'store.html',{'products':get_all_products,"comments":get_comments})


@login_required(login_url='/')
def add_product(request):
            
    
    return render(request,'add_product.html')
    









