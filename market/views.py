from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def aboutDetail(request):
    return render(request, 'about-detail.html')

def productDetail(request):
    return render(request, 'product-detail.html')

def productList1(request):
    return render(request, 'product-list1.html')

def productList2(request):
    return render(request, 'product-list2.html')

