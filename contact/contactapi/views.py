from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializers
from rest_framework import viewsets

# Create your views here.

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers