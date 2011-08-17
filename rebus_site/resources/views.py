from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from resources.models import Book, ExerciseMaterial, Publication, Journal, Link
from resources.models import BookForm, ExerciseForm, PubForm, JournalForm, LinkForm
from django.template import RequestContext
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from profilemgr.models import UserProfile


## Display views ##
def e_resources(request):    
    book_columns = ['Image', 'Title', 'Author', 'Link']
    exercise_columns = ['Title', 'Author', 'Type', 'Link']

    all_books = Book.objects.all().order_by('title')
    all_exercises = ExerciseMaterial.objects.all().order_by('title')
    
    return render(request, 'resources/eresources.html', {'books': all_books, 
                                                            'book_columns': book_columns,
                                                            'exercises': all_exercises,
                                                            'exercise_columns': exercise_columns})


def research(request):
    pub_columns = ['Title', 'Author', 'Link', 'Date']
    journal_columns = ['Title', 'Link']

    all_pubs = Publication.objects.all().order_by('title')
    all_journals = Journal.objects.all().order_by('title')
    
    return render(request, 'resources/research.html', {'pubs': all_pubs, 
                                                            'pub_columns': pub_columns,
                                                            'journals': all_journals,
                                                            'journal_columns': journal_columns})

def links(request):
    columns = ['Name', 'Description', 'Link']

    all_links = Link.objects.all().order_by('name')
    
    return render(request, 'resources/links.html', {'links': all_links, 
                                                       'columns': columns})

def community(request):
    columns = ['Picture', 'Name', 'Email', 'Location']

    # Only show active users with first_name and last_name
    all_people = UserProfile.objects.all().exclude(user__is_active=False).exclude(user__first_name="", 
                                                                                  user__last_name="").order_by('user__first_name')

    return render(request, 'resources/community.html', {'people': all_people, 'columns': columns})



## Update views ##
@login_required()
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/eresources/')
    else:
        form = BookForm()
    return render(request, 'resources/add_resource.html', {'form': form, 'title': 'book', 'url_name': '/add_book/'})


@login_required()
def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/eresources/')
    else:
        form = ExerciseForm()
    return render(request, 'resources/add_resource.html', {'form': form, 'title': 'exercise material', 'url_name': '/add_exercise/'})


@login_required()
def add_publication(request):
    if request.method == 'POST':
        form = PubForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/research/')
    else:
        form = PubForm()
    return render(request, 'resources/add_publication.html', {'form': form, 'title': 'publication', 'url_name': '/add_publication/'})


@login_required()
def add_journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/research/')
    else:
        form = JournalForm()
    return render(request, 'resources/add_resource.html', {'form': form, 'title': 'journal', 'url_name': '/add_journal/'})


@login_required()
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/links/')
    else:
        form = LinkForm()
    return render(request, 'resources/add_resource.html', {'form': form, 'title': 'link', 'url_name': '/add_link/'})
