from django.db import models
from django.forms import ModelForm


class Location(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.name


## Form based on the model ##

class LocationForm(ModelForm):
    class Meta:
        model = Location
