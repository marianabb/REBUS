from django.db import models

class GCalendar(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.name
    
