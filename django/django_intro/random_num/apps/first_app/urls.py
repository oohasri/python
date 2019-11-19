from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^display$', views.generate_random),
	url(r'^destroy$', views.destroy),
]