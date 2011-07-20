from django.shortcuts import render_to_response
from courses.models import Course
from courses.models import School
from courses.models import Lecturer


def courses(request):
    columns = ['Name', 'School', 'Lecturer', 'Language', 'Level', 'Type']

    all_courses = Course.objects.all().order_by('name')
    for c in all_courses:
        c.level = c.get_level_display()
        c.type = c.get_type_display()    

    return render_to_response('courses/courses.html', {'courses': all_courses, 'columns': columns})
    
