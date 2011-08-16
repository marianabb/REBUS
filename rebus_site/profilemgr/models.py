from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm
from easy_thumbnails.fields import ThumbnailerImageField

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # Extra fields
    url = models.URLField(verify_exists=False, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    work_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    # The directory 'avatars' in the media folder must exist
    image = ThumbnailerImageField(upload_to="avatars", blank=True, null=True, resize_source=dict(size=(100,100), sharpen=True))
    
    def __unicode__(self):
        return self.user.get_full_name() or self.user.username


## Form based on the previously defined model ##

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
