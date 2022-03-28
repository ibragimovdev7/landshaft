import json

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from rest_framework import viewsets, generics


class Serviceview(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ClientView(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

