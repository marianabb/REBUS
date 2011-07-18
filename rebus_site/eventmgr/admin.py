from eventmgr.models import Event
from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'beginning', 'end', 'location', 'language')

admin.site.register(Event, EventAdmin)
