from django.conf.urls import url
from . import views

urlpatterns = [
	urlpatterns(r'^$', views.index),
]