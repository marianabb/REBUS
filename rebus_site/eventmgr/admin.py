from eventmgr.models import GCalendar
from django.contrib import admin


class GCalAdmin(admin.ModelAdmin):
    list_display = ('link',)

admin.site.register(GCalendar, GCalAdmin)
