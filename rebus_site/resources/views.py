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
