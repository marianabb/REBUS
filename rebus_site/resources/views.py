from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from resources.models import Book, ExerciseMaterial, Publication, Journal, Link
from resources.models import BookForm, ExerciseForm, PubForm, JournalForm, LinkForm
from django.template import RequestContext
from django.core.files.storage import default_storage

## Display views ##
def e_resources(request):    
    book_columns = ['Image', 'Title', 'Author', 'Link']
    exercise_columns = ['Title', 'Author', 'Type', 'Link']

    all_books = Book.objects.all().order_by('title') #TODO the picture MUST be shown as thumbnail size!
    all_exercises = ExerciseMaterial.objects.all().order_by('title')
    #for e in all_exercises: #TODO remove
    #    e.type = e.get_level_display()
    
    return render_to_response('resources/eresources.html', {'books': all_books, 
                                                            'book_columns': book_columns,
                                                            'exercises': all_exercises,
                                                            'exercise_columns': exercise_columns})


def research(request):
    pub_columns = ['Title', 'Author', 'Link', 'Date']
    journal_columns = ['Title', 'Link']

    all_pubs = Publication.objects.all().order_by('title')
    all_journals = Journal.objects.all().order_by('title')
    
    return render_to_response('resources/research.html', {'pubs': all_pubs, 
                                                            'pub_columns': pub_columns,
                                                            'journals': all_journals,
                                                            'journal_columns': journal_columns})

def links(request):
    columns = ['Name', 'Description', 'Link'] #TODO perhaps truncate description (django filters)

    all_links = Link.objects.all().order_by('name')
    
    return render_to_response('resources/links.html', {'links': all_links, 
                                                       'columns': columns})


## Update views ##
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                path = settings.NEW_MEDIA_DIR + 'books/'
                default_storage.save(path, request.FILES['picture'])
            form.save()
            return HttpResponseRedirect('/eresources/')
    else:
        form = BookForm()
    return render_to_response('resources/add_resource.html', {'form': form, 'title': 'book', 'url_name': '/add_book/'},
                              context_instance=RequestContext(request))

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/eresources/')
    else:
        form = ExerciseForm()
    return render_to_response('resources/add_resource.html', {'form': form, 'title': 'exercise material', 'url_name': '/add_exercise/'},
                              context_instance=RequestContext(request))


def add_publication(request):
    if request.method == 'POST':
        form = PubForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/research/')
    else:
        form = PubForm()
    return render_to_response('resources/add_resource.html', {'form': form, 'title': 'publication', 'url_name': '/add_publication/'},
                              context_instance=RequestContext(request))


def add_journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/research/')
    else:
        form = JournalForm()
    return render_to_response('resources/add_resource.html', {'form': form, 'title': 'journal', 'url_name': '/add_journal/'},
                              context_instance=RequestContext(request))


def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/links/')
    else:
        form = LinkForm()
    return render_to_response('resources/add_resource.html', {'form': form, 'title': 'link', 'url_name': '/add_link/'},
                              context_instance=RequestContext(request))
