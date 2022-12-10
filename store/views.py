from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {
        'category': category
    }
    return render(request, 'category/collections.html', context)

def collectionView(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug = slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {
            'products': products,
            'category': category_name
        }
        return render(request, 'category/collectionView.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect ('collections')
    
def productView(request, slug):
    product = Product.objects.get(slug=slug)
    category_name = Category.objects.filter(product=product).first()
    context = {
       'product': product,
        'category': category_name
    }
    return render(request, 'category/productView.html', context)