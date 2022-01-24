from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.template import loader
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
import json
from .decorators import *
from .forms import *
# @allowed_users(roles=['admins'])
def index(request):
    products = Products.objects.all()
    category = Categories.objects.all()
    return render(request,'store/index.html',{'pd_list':products,'cat':category})
def categories(request):
    cat_list=Categories.objects.all()
    print(cat_list)
    template=loader.get_template("store/categories.html")
    context={'cat_list':cat_list,}
    return HttpResponse(template.render(context,request))
def products(request,cat_id):
    pd_list = Products.objects.filter(category=cat_id)
    template = loader.get_template("store/products.html")
    context = {'pd_list':pd_list,}
    return HttpResponse(template.render(context, request))
def order(request,pd_id):
    try:
        customer = Customer.objects.get(user=request.user)
        pd = Products.objects.get(id=pd_id)
        od=Order(customer=customer,order_date=datetime.now())
        od.save()
        ord_d = Order_details(customer=customer,product=pd, order=od, quantity=1)
        ord_d.save()
        return redirect('/')
    except Exception as e:
        client = Customer(user=request.user, email=request.user.email)
        client.save()
        pd=Products.objects.get(id=pd_id)
        od=Order(customer=client,order_date=datetime.now())
        od.save()
        ord_d = Order_details(customer=client,product=pd, order=od, quantity=1)
        ord_d.save()
        return redirect('/')
def box(request):
    try:
        client = Customer.objects.get(user=request.user)
        order_details = Order_details.objects.filter(customer=client)
        summ,total=0,0
        for i in order_details:
            summ+=i.get_total
            total+=i.quantity
        context = {
            'order_details': order_details,
            'summ':summ,
            'total':total
        }
        template = loader.get_template('store/box.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return HttpResponse('Hali hech narsa olinmadi')
def update_details(request):
    data = json.loads(request.body)
    customer, created = Customer.objects.get_or_create(user=request.user)
    customer.save()
    order, created = Order.objects.get_or_create(customer=customer)
    order.save()
    product = Products.objects.get(pk=data["product_id"])
    order_details,created = Order_details.objects.get_or_create(order=order, product=product)
    if data['action']=='add':
        print('res',data)
        order_details.quantity += 1
        order_details.save()
    else:
        print('res',data)
        order_details.quantity -= 1
        order_details.save()
    if order_details.quantity<=0:
        order_details.delete()
    #return JsonResponse("update amalga oshirildi",safe=False)
    return redirect('box')
def form(request):
    form=Form()
    print(form)
    context={
        'form':form
    }
    return render(request,'store/form.html',context)
def add_product(request):
    form = ProductForm()
    print(request.POST)
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'store/product_add.html', context)
@un_authintificated
def user_form(request):
    form=UserForm()
    print(form)
    form = UserForm(request.POST    )
    if form.is_valid():
        form.save()
        return redirect('login')
    context={
        'form':form
    }
    return render(request,'store/user.html',context)
def log_in(request):
    form = Login()
    username =request.POST.get('uname')
    password = request.POST.get('password')
   
    user = authenticate(request,username=username,password=password)
    if user:
        login(request,user)
        return redirect('/')
    else:
        print("was not logged!")
    context = {
        'form': form
    }
    return render(request,'store/Login/login.html')
# def customer(request):
#     customers=Customer.objects.all()
#     context={
#         'customers':customers
#     }
#     return render(request,'store/customer.html',context)
# def products_1(request):
#     pd_list = Products.objects.all()
#     template = loader.get_template("store/products.html")
#     context = {'pd_list':pd_list,}
#     return HttpResponse(template.render(context, request))

def create_user(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('uname')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
            user.save()
            return redirect('/login') 
    except Exception as e:
        pass
    return render(request,'store/Login/registration.html')

def buy(request,pd_id):
    return HttpResponse(pd_id)




