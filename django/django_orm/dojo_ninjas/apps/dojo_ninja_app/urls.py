from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^books_template$', views.template),
	url(r'^authors_template$', views.authors_template),
	url(r'^addbook$', views.addbook),
	url(r'^book/(?P<my_val>\d+)$', views.display_book),
	url(r'^addauthor_to_book$', views.add_new_author),
	url(r'^author/(?P<my_val>\d+)$', views.display_author),
	url(r'^addauthor$', views.addauthor),
	url(r'^addbook_to_author$', views.add_new_book),
]
