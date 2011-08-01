from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from locations.models import Location
from django.core import serializers


def show_map(request):
    init_coord = settings.MAP_INIT_LAT + ',' + settings.MAP_INIT_LON
    init_zoom = settings.MAP_ZOOM

    locations = serializers.serialize('json', Location.objects.all(), fields=('name', 'latitude', 'longitude'))    

    return render(request, 'map/map.html', {'init_coord': init_coord, 'init_zoom': init_zoom, 
                                               'locations': locations, 'locations_size': len(Location.objects.all())})
