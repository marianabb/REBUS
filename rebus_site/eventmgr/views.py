from django.shortcuts import render
from eventmgr.models import GCalendar
from django.template import RequestContext


def show_calendar(request):
    colors = ['blue', 'brown', 'green', 'purple', 'red', 'grey', 'black']
    links = ', '.join(('{url: "%s", color: "%s"}' % (cal.link, colors[i % len(colors)])) 
                      for (i, cal) in enumerate(GCalendar.objects.all()))
    
    return render(request, 'calendar/calendar.html', {'calendar_links': links})
