from profilemgr.models import UserProfile
from registration.models import RegistrationProfile
from django.contrib import admin

admin.site.register(UserProfile)

# Delete RegistrationProfile from the admin site
#admin.site.unregister(RegistrationProfile)
