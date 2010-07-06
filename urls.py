# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from settings import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

print project_path+'/digi/media/css/'

urlpatterns = patterns('',
    (r'^/?$', 'cqtc.digi.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(project_path, 'digi/media'), 'show_indexes': True}),
        #settings.STATIC_DOC_ROOT
    )
