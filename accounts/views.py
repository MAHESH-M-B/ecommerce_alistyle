from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer

class AccountViewset(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset=Account.objects.all()