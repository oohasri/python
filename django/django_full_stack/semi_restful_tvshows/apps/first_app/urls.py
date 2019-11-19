from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.all_shows),
	url(r'^shows$', views.all_shows),
	url(r'^shows/new$', views.add_show),
	url(r'^shows/create$', views.create_show),
	url(r'^shows/(?P<my_val>\d+)$', views.display_show),
	url(r'^shows/(?P<my_val>\d+)/edit$', views.edit_show),
	url(r'^shows/(?P<my_val>\d+)/delete$', views.delete_show),
	url(r'^shows/update$', views.update)
]