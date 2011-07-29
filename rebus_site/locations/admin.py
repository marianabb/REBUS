from locations.models import Location
from django.contrib import admin


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)

admin.site.register(Location, LocationAdmin)
