from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^login_success$', views.success),
	url(r'^logout$', views.destroy),
	url(r'^wall$', views.user_wall),
	url(r'^comment$', views.post_comment),
	url(r'^submit_post$', views.post_submit),
	url(r'^delete_message', views.message_delete),
]