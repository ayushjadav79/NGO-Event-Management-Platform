from django.contrib import admin
from .models import NGO

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'contact_person', 'city', 'state')
    search_fields = ('name', 'registration_number', 'contact_person')
    list_filter = ('city', 'state')