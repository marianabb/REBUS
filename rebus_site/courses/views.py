from django.shortcuts import render
from django.http import HttpResponseRedirect
from courses.forms import LayoutCourseForm
from courses.models import Course
from profilemgr.models import UserProfile
from django.template import RequestContext

from django.contrib.auth.decorators import login_required


def courses(request):
    columns = ['Name', 'School', 'Lecturer', 'Language', 'Level', 'Type']
    all_courses = Course.objects.all().order_by('name') 

    return render(request, 'courses/courses.html', {'courses': all_courses, 'columns': columns})
  

@login_required()
def add_course(request):
    if request.method == 'POST':
        form = LayoutCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/courses/')
    else:
        form = LayoutCourseForm()
    return render(request, 'courses/add_course.html', {'form': form, 'title': 'course', 'url_name': '/add_course/'})
