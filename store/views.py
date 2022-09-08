from django.shortcuts import render
from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products, 'categories': categories})
