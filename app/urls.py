from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # User module
	url(r'^index/',  'app.views_users.index',  name='index'),
    url(r'^login/',  'app.views_users.sigin',  name='login'),
    url(r'^logout/', 'app.views_users.sigout', name='logout'),    
	
	# DB Exporter module
	url(r'^connection/add/',                     'app.views_export.add_connect',  name='connection-add'),
	url(r'^connection/list/',                    'app.views_export.list_connect', name='connection-list'),
	url(r'^connection/edit/(?P<conn_id>\d+)/$',  'app.views_export.edit_connect', name='connection-edit'),
	
	url(r'^export/', 'app.views_export.export', name='export'),
	url(r''),
)
