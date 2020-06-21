from django.contrib import admin
from . models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'designation', 'created_date')
    list_filter =   ('designation',)
    list_display_links = ('firstname', 'lastname',)
    search_fields = ('firstname', 'lastname', 'designation')

admin.site.register(Team, TeamAdmin)
