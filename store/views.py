from django.shortcuts import render
from rest_framework import viewsets
from .models import Store
from .serializers import StoreSerializer
# Create your views here.

class StoreViewset(viewsets.ModelViewSet):
    serializer_class=StoreSerializer
    queryset=Store.objects.all()