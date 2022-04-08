from django.shortcuts import render, get_object_or_404
from category.models import Category
from store.models import Product


def store(request, category_slug=None):
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products
    }
    return render(request, 'store.html', context=context)

def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        'single_product': single_product
    }
    return render(request, 'product-detail.html', context=context)
