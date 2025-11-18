from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'ngo', 'date_time', 'location_city')
    list_filter = ('location_city', 'location_state', 'ngo')
    search_fields = ('title', 'ngo__name')
    autocomplete_fields = ['ngo']