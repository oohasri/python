from django.db import models
import re
from datetime import datetime, date

class UserManager(models.Manager):
    def basic_validator(self, postData):        
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME = re.compile(r'^[a-zA-Z]+$')
        # add keys and values to errors dictionary for each invalid field
        if not NAME.match(postData['first_name']) or len(postData['first_name']) < 2:
            errors["first_name"] = "Invalid First name"
        if not NAME.match(postData['alias']) or len(postData['alias']) < 2:
            errors["alias"] = "Invalid Last name"
        if not EMAIL_REGEX.match(postData['email']) or len(postData['email']) < 10:    # test whether a field matches the pattern            
            errors['email_invalid'] = "Invalid email address!"
        if len(postData['password']) < 8 or postData['password']!=postData['confirm_password']:
            errors["password"] = "Invalid password/Password doesn't match"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']) or len(postData['email']) < 10:    # test whether a field matches the pattern            
            errors['email_invalid'] = "Invalid email address!"
        if len(postData['password']) <= 8:
            errors["password"] = "Invalid password"
        return errors

    def post_validator(self, postData):
        errors = {}
        if len(postData['content']) < 5:
            errors["invalid_post"] = "Invalid post"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line!

class Author(models.Model):
    author_name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length = 45)
    user = models.ForeignKey(User, related_name = "user_books")
    author = models.ForeignKey(Author , related_name = "books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User , related_name = "reviews")
    book = models.ForeignKey(Book, related_name = "book_reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
