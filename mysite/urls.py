from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()
from views import hello, current_datetime,hours_ahead,display_meta,thanks,link
from books import views
from contact.views import contact

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$',hello),
    ('^time/$', current_datetime),
    ('^another-time-page/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
	(r'^browser/$',display_meta),
	#url(r'^search-form/$', views.search_form),
	(r'^search/$', views.search),
	(r'^contact/$', contact),
	(r'^contact/thanks/$', thanks),
	(r'^link/$', link),
)

urlpatterns += patterns((''),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/project/djcode/mysite/mysite/static'}
    ),
)