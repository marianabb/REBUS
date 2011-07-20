from django.db import models

class Lecturer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    url = models.URLField(verify_exists=False, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    work_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    #image = models.FileField(upload_to="media", blank=True, null=True) TODO
    
    def __unicode__(self):
        return self.first_name+' '+self.last_name

class School(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(verify_exists=False)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(verify_exists=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=30) #Language of instruction
    LEVEL_CHOICES = (
        (u'bg', u'Beginner'),
        (u'im', u'Intermediate'),
        (u'ad', u'Advanced'),
        (u'ph', u'Phd')
        )
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    TYPE_CHOICES = (
        (u'ca', u'Campus'),
        (u'on', u'Online'),
        (u'bl', u'Blended')
        )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    # Every school can have many courses
    school = models.ForeignKey(School)
    # Every lecturer can have many courses
    lecturer = models.ForeignKey(Lecturer)

    def __unicode__(self):
        return self.name

