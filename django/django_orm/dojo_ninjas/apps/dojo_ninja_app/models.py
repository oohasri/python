from django.db import models

class dojo(models.Model):
	name = models.CharField(max_length = 255)
	city = models.CharField(max_length = 255)
	state = models.CharField(max_length = 2)
	desc = models.TextField(default="")
	#dojo has many ninjas(one->many)dojo->ninjas

class ninjas(models.Model):
	dojo_id = models.ForeignKey(dojo, related_name = "ninjas")
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)

class Book(models.Model):
	title = models.CharField(max_length = 255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	books = models.ManyToManyField(Book, related_name="authors")
	notes = models.TextField(default="Some notes")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
# Create your models here.
