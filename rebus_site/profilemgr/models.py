from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # Extra fields
    url = models.URLField(verify_exists=False, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    work_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    image = models.FileField(upload_to="avatars", blank=True, null=True)
    
    def __unicode__(self):
        return self.user.get_full_name() or self.user.username

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)


# Function to create a UserProfile when a User is created
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
