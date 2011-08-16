from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from locations.models import Location, LocationForm
from django.core import serializers
from django.contrib.auth.decorators import login_required


def show_map(request):
    init_coord = settings.MAP_INIT_LAT + ',' + settings.MAP_INIT_LON
    init_zoom = settings.MAP_ZOOM

    locations = serializers.serialize('json', Location.objects.all(), fields=('name', 'latitude', 'longitude'))    

    return render(request, 'map/map.html', {'init_coord': init_coord, 'init_zoom': init_zoom, 
                                               'locations': locations, 'locations_size': len(Location.objects.all())})


@login_required()
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/map/')
    else:
        form = LocationForm()
    # using the same template as all other resources
    return render(request, 'resources/add_resource.html', {'form': form, 'title': 'location', 'url_name': '/add_location/'})   
