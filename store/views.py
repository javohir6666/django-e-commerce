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
    
def productView(request, category_slug, product_slug):
    if(Category.objects.filter(slug=category_slug, status=0)):
        if(Product.objects.filter(slug=product_slug, status=0)):
            products = Product.objects.filter(slug=product_slug, status=0).first
            context = {
                'products' : products
            }
        else:
            messages.error(request, "No such category found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request, 'category/productView.html', context)