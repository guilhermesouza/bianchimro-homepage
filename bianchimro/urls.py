import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bianchimro.views.home', name='home'),
    # url(r'^bianchimro/', include('bianchimro.foo.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^comments/', include('django.contrib.comments.urls')),
    #(r'^gallery/', include('imagestore.urls', namespace='imagestore')),

    (r'^tinymce/', include('tinymce.urls')),

    #cms urls
    url(r'^', include('cms.urls')),
    url(r'^', include('cms.urls', namespace='imagestore')),
    url(r'^blog/', include('zinnia.urls')),    

    
)


if settings.DEBUG or True:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns

"""
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
"""

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()


#overrides
import overrides.zinnia_moderation


