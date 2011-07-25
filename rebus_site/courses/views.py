from django.shortcuts import render_to_response
from courses.models import Course
from courses.models import School
from profilemgr.models import UserProfile
from django.template import RequestContext


def courses(request):
    columns = ['Name', 'School', 'Lecturer', 'Language', 'Level', 'Type']
    all_courses = Course.objects.all().order_by('name') 

    return render_to_response('courses/courses.html', {'courses': all_courses, 'columns': columns},
                              context_instance=RequestContext(request))
  
