from django.db import models

# Models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    org_numer = models.CharField(max_length=255, blank=True, null=True)
    first_invoice_number = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, related_name="teams", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        
    def __str__(self):
        return '%s' % self.name