from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Product
from django.views.generic import DetailView, ListView

# Create your views here.


def home(request):
    return render(request, 'home.html')


# def order(request, id):
#     order = User.objects.get(id=id)
#     return render(request, 'order.html', {'order: order'})


def product_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})


def order_view(request):
    return render(request, 'order.html')


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/detail.html', {'product': product})


def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    print("The account has been disabled.")
                    return redirect('/')
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
