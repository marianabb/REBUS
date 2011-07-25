from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import create_update
from django.conf import settings
from resources.models import Book, ExerciseMaterial
from registration.views import register
from profilemgr import regbackend
from profilemgr.forms import UserProfileForm
import registration.backends.default.urls as regUrls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


book_info = {
    "model": Book,
    "post_save_redirect": "/add_book/",
    "login_required": False, #TODO should be true later
    }

urlpatterns = patterns('',
                       url(r'^$', direct_to_template, {'template':'home.html'}),

                       # Display views
                       url(r'^courses/$', 'rebus_site.courses.views.courses'),
                       url(r'^eresources/$', 'rebus_site.resources.views.e_resources'),
                       url(r'^research/$', 'rebus_site.resources.views.research'),
                       url(r'^links/$', 'rebus_site.resources.views.links'),

                       # Update views
                       url(r'^add_book/$', 'rebus_site.resources.views.add_book', name='add_book'),
                       url(r'^add_exercise/$', 'rebus_site.resources.views.add_exercise', name='add_exercise'),
                       url(r'^add_publication/$', 'rebus_site.resources.views.add_publication', name='add_publication'),
                       url(r'^add_journal/$', 'rebus_site.resources.views.add_journal', name='add_journal'),
                       url(r'^add_link/$', 'rebus_site.resources.views.add_link', name='add_link'),

                       # Django-profiles
                       #(r'^profiles/', include('profiles.urls')),

                       # Django-registration
                       url(r'^accounts/register/$', register, {'backend': 'registration.backends.default.DefaultBackend','form_class': UserProfileForm}, name='registration_register'),
                       (r'^accounts/', include(regUrls)),

                       # Uncomment the admin/doc line below to enable admin documentation:
                           url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
                       )
