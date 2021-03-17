from rest_framework import serializers

# Models
from .models import Invoice, Item


class InvoiceSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        read_only_fields = ['team', 'created_at', 'created_by', 'modified_by', 'modified_at']
        fields = '__all__'