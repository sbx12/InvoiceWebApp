from rest_framework import serializers

# Models
from .models import Team


class TeamSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = ['created_by']
        fields = '__all__'