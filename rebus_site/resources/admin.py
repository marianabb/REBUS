from resources.models import Book
from resources.models import ExerciseMaterial
from resources.models import Publication
from resources.models import Journal
from resources.models import Link
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link') #TODO Maybe we would like to display picture

admin.site.register(Book, BookAdmin)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link', 'type')

admin.site.register(ExerciseMaterial, ExerciseAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'link', 'date')

admin.site.register(Publication, PublicationAdmin)


class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

admin.site.register(Journal, JournalAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

admin.site.register(Link, LinkAdmin)
