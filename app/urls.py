from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # User module
                       url(r'^index/', 'app.views_users.index', name='index'),
                       url(r'^login/', 'app.views_users.signin', name='login'),
                       url(r'^logout/', 'app.views_users.signout', name='logout'),

                       # DB Tools module
                       url(r'^config/$', 'app.views_export.config', name='db-config'),
                       url(r'^config/add/$', 'app.views_export.config_add', name='db-config-add'),
                       url(r'^config/edit/(?P<conn_id>\d+)$', 'app.views_export.config_edit', name='db-config-edit'),
                       url(r'^config/delete/(?P<conn_id>\d+)$', 'app.views_export.config_delete',
                           name='db-config-delete'),

                       url(r'^exporter/', 'app.views_export.exporter', name='db-exporter'),
                       url(r'^parser/', 'app.views_export.parser', name='db-parser'),
                       )
