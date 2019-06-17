# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import product,Contact
from math import ceil
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
def index(request):
    allProds = []
    catprods = product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product1 = product.objects.filter(product_id=myid)


    return render(request, 'shop/prodView.html', {'product':product1[0]})
def checkout(request):
    return render(request, 'shop/checkout.html')

# Create your views here.
