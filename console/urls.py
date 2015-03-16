from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^index/',  'console.views.index',  name='index'),
    url(r'^login/',  'console.views.sigin',  name='login'),
    url(r'^logout/', 'console.views.sigout', name='logout'),    
)
