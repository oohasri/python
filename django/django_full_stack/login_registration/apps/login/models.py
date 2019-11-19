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
        if not NAME.match(postData['last_name']) or len(postData['last_name']) < 2:
            errors["last_name"] = "Invalid Last name"
        if  not postData['age'] or postData['age'] >= date.today().strftime("%Y-%m-%d"):
            errors["age"] = "Invalid age"
        if postData['age']:
            today = date.today()        
            my_bday = datetime.strptime(postData['age'], '%Y-%m-%d').date()
            age = today.year - my_bday.year - ((today.month, today.day) < (my_bday.month, my_bday.day))
            if age<13:
                errors["age_invalid"] = "You are under age 13"
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
    last_name = models.CharField(max_length = 45)
    birthday = models.DateField(default = '2000-01-01')
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line!

class Message(models.Model):
    user = models.ForeignKey(User, related_name="users")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name="messages")
    user_id = models.ForeignKey(User, related_name="commentor")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

# Create your models here.
