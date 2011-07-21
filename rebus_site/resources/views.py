from django.shortcuts import render_to_response
from resources.models import Book
from resources.models import ExerciseMaterial
from resources.models import Publication
from resources.models import Journal
from resources.models import Link


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
