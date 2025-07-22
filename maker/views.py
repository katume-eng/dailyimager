from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Product

def init(request):
    return HttpResponse("Welcome to the Maker App!")

def user_list(request):
    users = User.objects.all()
    return render(request, 'maker/user_list.html', {'users': users})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'maker/product_list.html', {'products': products})

