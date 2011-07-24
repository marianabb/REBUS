from django.db import models
from django.forms import ModelForm

## Educational Resources
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    picture = models.FileField(upload_to="books", blank=True, null=True) # TODO change to image, change filename perhaps
    link = models.URLField(verify_exists=False, blank=True, null=True)

    def __unicode__(self):
        return self.title
    
    
class ExerciseMaterial(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(verify_exists=False)
    TYPE_CHOICES = (
        (u're', u'Reading'),
        (u'sp', u'Speaking'),
        (u'li', u'Listening'),
        (u'gr', u'Grammar')
        )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __unicode__(self):
        return self.title


## Research Resources
class Publication(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    link = models.URLField(verify_exists=False)
    date = models.DateField()

    def __unicode__(self):
        return self.title


class Journal(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(verify_exists=False)

    def __unicode__(self):
        return self.title


## Useful Links
class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(verify_exists=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


## Forms based on the previously defined models ##

class BookForm(ModelForm):
    class Meta:
        model = Book


class ExerciseForm(ModelForm):
    class Meta:
        model = ExerciseMaterial


class PubForm(ModelForm):
    class Meta:
        model = Publication


class JournalForm(ModelForm):
    class Meta:
        model = Journal


class LinkForm(ModelForm):
    class Meta:
        model = Link
