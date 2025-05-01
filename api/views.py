from django.shortcuts import render
from rest_framework import generics
from core.models import *
from .serialisers import *

# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

