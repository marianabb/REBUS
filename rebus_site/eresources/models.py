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
    
    def __unicode__(self):
        return self.first_name+' '+self.last_name

class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_url = models.URLField(verify_exists=False)
    school_email = models.EmailField(blank=True, null=True)
    school_phone = models.CharField(max_length=20, blank=True, null=True)
    school_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.school_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_url = models.URLField(verify_exists=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=30) #Language of instruction
    LEVEL_CHOICES = (
        (u'bg', u'Beginner'),
        (u'im', u'Intermediate'),
        (u'ad', u'Advanced')
        )
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)

    # Every school can have many courses
    school = models.ForeignKey(School)
    # Every lecturer can have many courses
    lecturer = models.ForeignKey(Lecturer)

    def __unicode__(self):
        return self.course_name

    




