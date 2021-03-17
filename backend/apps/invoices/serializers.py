from rest_framework import serializers

# Models
from .models import Invoice, Item


class ItemSerialzier(serializers.ModelSerializer):    
    class Meta:
        model = Item
        read_only_fields = ['invoice']
        fields = '__all__'


class InvoiceSerialzier(serializers.ModelSerializer):
    items = ItemSerialzier(many=True)
    
    class Meta:
        model = Invoice
        read_only_fields = ['team', 'created_at', 'created_by', 'modified_by', 'modified_at']
        fields = '__all__'
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)
        
        for item in items_data:
            Item.objects.create(invoice=invoice, **item)
            
        return invoice