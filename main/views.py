from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from requests import request
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt 



# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Item.objects.filter(user=request.user)
    products_count = products.count()
    context = {
        'name': request.user.username,
        'products': products,
        'products_count': products_count,
        'image_url' : 'https://i0.wp.com/www.petmania.ie/wp-content/uploads/2023/04/MP20774_Petmania_Whiskas_Brand-page-612x435-Mobile.jpg?fit=612%2C435&ssl=1',
        'last_login': request.COOKIES['last_login'],
        }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def add_product(request, product_id):
    if request.method == 'POST' and 'Tambah' in request.POST:
        product = Item.objects.get(id = product_id)
        product.amount += 1
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_product(request, product_id):
    if request.method == 'POST' and 'Kurang' in request.POST:
        product = Item.objects.get(id = product_id)
        if product.amount > 0 :
            product.amount -= 1
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def remove_product(request, product_id):
    if request.method == 'POST' and 'Hapus' in request.POST:
        product = Item.objects.get(id = product_id)
        product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
    
@login_required(login_url='/login')
def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        pet = request.POST.get("pet")
        product = request.POST.get("product")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        image = request.POST.get("image")
        user = request.user

        new_product = Item(pet=pet, product=product, price=price, description=description, amount=amount, image=image, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()