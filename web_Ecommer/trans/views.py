from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from rest_framework import  permissions
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from ecom.models import Category,Laptop,Book,Shoe,User,Author,Brand,Publisher,Producer,Product,Cart,CartItem,Order
# Create your views here.
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request,'login.html',)



def position_check(user):
    return user.is_superuser
@login_required
@user_passes_test(position_check,"/")
def get_home(request):
        return render(request, "content.html")

@login_required
@user_passes_test(position_check,"/")
def get_User(request):
        return render(request, "admin/User/index.html")

@login_required
@user_passes_test(position_check,"/")
def get_category(request):
    return  render(request, "admin/Category/index.html")

@login_required
@user_passes_test(position_check,"/")
def get_Producer(request):
    return render(request,"admin/Producer/index.html")

@login_required
@user_passes_test(position_check,"/")
def get_Order(request):
    return render(request, "admin/Order/index.html")

@login_required
@user_passes_test(position_check,"/")
def get_Brand(request):
    return render(request,"admin/Brand/index.html")

@login_required
@user_passes_test(position_check,"/")
def get_Publisher(request):
    return render(request,"admin/Publisher/index.html")

@login_required
@user_passes_test(position_check,"/")
def get_Laptop(request):
    categoty= Category.objects.filter()
    producer= Producer.objects.filter()
    return render(request,"admin/Laptop/index.html",{'category':categoty, 'producer':producer})

@login_required
@user_passes_test(position_check,"/")
def get_Shoe(request):
    categoty= Category.objects.filter()
    brand= Brand.objects.filter()
    return render(request,"admin/Shoe/index.html",{'category':categoty, 'brand':brand})

@login_required
@user_passes_test(position_check,"/")
@user_passes_test(position_check,login_url="/")
def get_Book(request):
    categoty= Category.objects.filter()
    publisher= Publisher.objects.filter()
    author=Author.objects.filter()
    return render(request,"admin/Book/index.html",{'category':categoty, 'publisher':publisher,'author':author})

@login_required
@user_passes_test(position_check,"/")
def get_Author(request):
    return render(request,"admin/Author/index.html")

#login


class SiteLoginView(LoginView,):
    template_name = 'login.html'
    redirect_field_name = 'home'

def Register(request):
    return render(request,"register.html")
#
# client
def gethomeclient(request):
    return render(request,'client/listProduct.html')

def getProductDetail(request,id):
    product= Product.objects.filter(id=id)
    return render(request,"client/productdetail.html",{'product':product})

def getListCartItem(request):
    return render(request,'client/listCartItem.html')

def getOrderadd(request):
    return render(request,'client/OrderAdd.html')

@login_required()
def deletecard(request):
    card=Cart.objects.get(User=request.user.id)
    carditem =CartItem.objects.filter(Cart=card)
    carditem.delete()
    return HttpResponseRedirect('/cart/')

def getOrderlist(request):
    return render(request,'client/listOrder.html')

def getListLaptop(request):
    laptop = Laptop.objects.filter()
    return render(request,'client/list.html',{'laptop':laptop})
def getListBook(request):
    book = Book.objects.filter()
    return render(request,'client/list.html',{'book':book})

def getListShoe(request):
    shoe = Shoe.objects.filter()
    return render(request,'client/list.html',{'shoe':shoe})

def getupdateDanggiao(request,id):
    order = Order.objects.filter(id=id).update(status=1)
    return render(request,'admin/Order/index.html')

def getupdatetc(request,id):
    order = Order.objects.filter(id=id).update(status=2)
    return render(request,'admin/Order/index.html')

def getProductsearch(request):
    if request.POST:
        inputsearch = request.POST['search']
        product = Product.objects.filter(name__contains=inputsearch)
    return render(request,"client/listSearch.html",{'product':product})
