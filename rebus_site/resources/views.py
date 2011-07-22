from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from resources.models import Book, ExerciseMaterial, Publication, Journal, Link
from resources.models import BookForm
from django.template import RequestContext


def e_resources(request):
    book_columns = ['Image', 'Title', 'Author', 'Link']
    exercise_columns = ['Title', 'Author', 'Type', 'Link']

    all_books = Book.objects.all().order_by('title') #TODO the picture MUST be shown as thumbnail size!
    all_exercises = ExerciseMaterial.objects.all().order_by('title')
    for e in all_exercises:
        e.type = e.get_level_display()
    
    return render_to_response('resources/eresources.html', {'books': all_books, 
                                                            'book_columns': book_columns,
                                                            'exercises': all_exercises,
                                                            'exercise_columns': exercise_columns},
                              context_instance=RequestContext(request)) #TODO is this necessary?


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


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print "FILEEE", request.FILES['picture']
            handle_uploaded_file(request.FILES['picture'])
            form.save()
            return HttpResponseRedirect('/eresources/')
    else:
        form = BookForm()
    return render_to_response('resources/add_book.html', {'form': form},
                              context_instance=RequestContext(request)) #TODO is this ok here?


def handle_uploaded_file(f):
    destination = open('/Users/mariana/Documents/Work/REBUS/rebus_site/media/books/'+str(f), 'wb+') # TODO Better way!
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
