from rest_framework import serializers
from .models import *
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()