from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from .serializers import TeamSerialzier

# Models
from .models import Team


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerialzier
    queryset = Team.objects.all()
    
    def get_queryset(self):
        if not self.request.user.teams.all().exists():
            Team.objects.create(name='Test Team', org_numer=9110, created_by=self.request.user)

        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def perform_update(self, serializer):
        obj = self.get_object()
        
        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object Owner')
        
        serializer.save()
        
