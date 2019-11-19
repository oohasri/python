from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^login_success$', views.success),
	url(r'^wall$', views.user_wall),
	url(r'^addbook$', views.add_book),
	url(r'^post_book$', views.book_post),
	url(r'^display_book$', views.book_display),
	url(r'^submit_review$', views.review_submit),
	url(r'^logout$', views.destroy),
]