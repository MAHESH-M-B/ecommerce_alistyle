from django.shortcuts import render
from store.models import Store
def home(request):
    products=Store.objects.all().filter(is_available=True)
    products_count = products.count()
    context={
        'products':products,
        'products_count': products_count,
    }
    return render(request, 'index.html' ,context)