from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', direct_to_template, {'template':'home.html'}),
                       url(r'^courses/$', 'rebus_site.courses.views.courses'),
                       url(r'^eresources/$', 'rebus_site.resources.views.e_resources'),
                       url(r'^research/$', 'rebus_site.resources.views.research'),
                       url(r'^links/$', 'rebus_site.resources.views.links'),
                       

                       # Uncomment the admin/doc line below to enable admin documentation:
                           url(r'^admin/doc/', include('django.contrib.admindocs.urls')),                       
                       # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
                       )


# TODO this is only for development
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                }),
                            )
    
