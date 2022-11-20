from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Store
from category.models import Category
from .serializers import StoreSerializer
# Create your views here.

def store(request,category_slug=None):
    categories=None
    products=None
    if category_slug != None:
        categories=get_object_or_404(Category,category_slug=category_slug)
        products=Store.objects.filter(category=categories,is_available=True)
        products_count=products.count()
        context={
        'products':products,
        'products_count':products_count, 
        }
    else:
        products=Store.objects.all().filter(is_available=True)
        products_count=products.count()
        context={
            'products':products,
            'products_count':products_count,
        }
    return render(request,'store/store.html' , context)



class StoreViewset(viewsets.ModelViewSet):
    serializer_class=StoreSerializer
    queryset=Store.objects.all()