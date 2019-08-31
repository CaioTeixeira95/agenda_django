"""Information for Django admin page."""

from django.contrib import admin
from core.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    """This class is for admin page of Django."""
    list_display = ('id', 'title', 'event_date', 'created_date')
    list_filter = ('title', 'user')

admin.site.register(Event, EventAdmin)
