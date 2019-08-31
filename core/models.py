"""Models of the project."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    """This is the model of the event."""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title

    def get_event_date(self):
        """Format the presentation of the event date."""
        return self.event_date.strftime('%d/%m/%Y %H:%Mh')

    def get_event_date_input(self):
        """Format the presentation of the event date for HTML input type datetime-local."""
        return self.event_date.strftime('%Y-%m-%dT%H:%M')
