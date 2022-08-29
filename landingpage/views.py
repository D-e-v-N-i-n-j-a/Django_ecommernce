from email import message
from pydoc import describe
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Reviews,Products
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.





def landingpage(request):
    all_products = Products.objects.all()
    
    return render(request,'index.html',{'products':all_products})




def product_details(request,pk):
    user = auth.get_user(request)
    get_product  = Products.objects.get(id=pk)
    if request.method =='POST':
        describe = request.POST['message']
        if user.is_authenticated and describe != '':
           comment_object = Reviews.objects.create(description = describe,user=user,product_fk = get_product)
           comment_object.save()
           print('comment added successfully')
           return HttpResponseRedirect(request.path_info)
            
        else:
            print('failed')
            return redirect('product_details')
    getReviews = Reviews.objects.filter(product_fk=get_product)
    
    return render(request,'product_details.html',{'user':user,"product":get_product,'review':getReviews})



    


