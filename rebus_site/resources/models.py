from django.db import models

## Educational Resources
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    picture = models.FileField(upload_to="media", blank=True, null=True) # TODO details
    link = models.URLField(verify_exists=False, blank=True, null=True)

    def __unicode__(self):
        return self.book_title
    
    
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
        return self.ex_title


## Research Resources
class Publication(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    link = models.URLField(verify_exists=False)
    date = models.DateField()

    def __unicode__(self):
        return self.pub_title


class Journal(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(verify_exists=False)

    def __unicode__(self):
        return self.journal_title


## Useful Links
class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(verify_exists=False)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
