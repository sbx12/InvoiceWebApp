from rest_framework import serializers

# Models
from .models import Client


class ClientSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = ['created_at','created_by']
        fields = '__all__'