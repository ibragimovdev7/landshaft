from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets

class Serviceview(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
