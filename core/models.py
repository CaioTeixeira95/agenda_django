from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
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

    def get_created_date(self):
        return self.created_date.strftime('%d/%m/%Y %H:%Mh')
