from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from .serializers import ClientSerialzier

# Models
from .models import Client


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerialzier
    queryset = Client.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def perform_update(self, serializer):
        obj = self.get_object()
        
        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object Owner')
        
        serializer.save()