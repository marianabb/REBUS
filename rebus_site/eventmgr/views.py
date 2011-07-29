from django.shortcuts import render_to_response
from eventmgr.models import GCalendar
from django.template import RequestContext


def show_calendar(request):
    colors = ['blue', 'brown', 'green', 'purple', 'red', 'grey', 'black']
    links = ', '.join(('{url: "%s", color: "%s"}' % (cal.link, colors[i % len(colors)])) 
                      for (i, cal) in enumerate(GCalendar.objects.all()))
    
    return render_to_response('calendar/calendar.html', {'calendar_links': links},
                              context_instance=RequestContext(request))
