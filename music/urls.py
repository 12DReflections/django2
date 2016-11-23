from django.conf.urls import include, url
from . import views



urlpatterns = [
		#/music/
	url('^$', views.index, name='index'),
		
		#/music/712  (?P<foo>) creates an object foo, 
		#              pull out the number before the slash,
		# 			   treat as album_id
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]