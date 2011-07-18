from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    beginning = models.DateField()
    end = models.DateField()
    location = models.TextField()
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.event_name
