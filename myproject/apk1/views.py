
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *

def say_hello(request):
    return render(request, 'main.html')

#def home(request):
    #return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully!')
            #image= form.cleaned_data.get('img')
            #messages.success(request, f'{image}')
            return redirect('main.html')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

def collections(request):
    category = Category.objects.all()
    #category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products =Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first
        context = {'products' : products, 'category_name':category_name}
        return render(request, "products/index.html", context)
    else:
        messages.warning(request, "no such products")
        return redirect('collections.html')

