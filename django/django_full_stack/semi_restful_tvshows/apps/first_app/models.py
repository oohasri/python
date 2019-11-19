from django.db import models
from datetime import datetime, date

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3:
            errors["title"] = "Title should be at least 3 characters"
        if len(postData['network']) < 3:
        	errors["network"] = "Network should be at least 3 characters"
        if len(postData['date']) != 10:
        	if postData['date'] >= date.today():
        		errors["release_date"] = "Date is invalid"
        if len(postData['description']) == None:
        	errors["description"] = "description should be at least 10 characters"        
        return errors

class Show(models.Model):
	title = models.CharField(max_length = 45)
	network = models.CharField(max_length = 45)
	release_date = models.DateField()
	description = models.TextField()
	objects = BlogManager()    # add this line!
# Create your models here.

