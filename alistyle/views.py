from django.shortcuts import render
from store.models import Store
def home(request):
    products=Store.objects.all().filter(is_available=True)
    context={
        'products':products
    }
    return render(request, 'index.html' ,context)