# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import product,Contact,Orders
from math import ceil
import logging
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout


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
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product1 = product.objects.filter(product_id=myid)
    return render(request, 'shop/prodview.html', {'product':product1[0]})
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST.get('usern1','')
        email = request.POST.get('usern', '')
        password=request.POST.get('passw','')
        user=User.objects.create_user(username,email,password)
        user.save()

        return redirect('/shop')
    return redirect('/shop')
def signin(request):
    if request.method=="POST":
        email = request.POST.get('su', '')
        password=request.POST.get('sv','')
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/shop')
        else:
            return redirect('/contact')


