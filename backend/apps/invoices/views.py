from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from .serializers import InvoiceSerialzier

# Models
from .models import Invoice, Item


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerialzier
    queryset = Invoice.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        serializer.save(created_by=self.request.user, team=team)
        
    def perform_update(self, serializer):
        obj = self.get_object()
        
        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object Owner')
        
        serializer.save()