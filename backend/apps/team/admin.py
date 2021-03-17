from django.contrib import admin

# Models
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
