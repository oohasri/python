from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, "first_app/index.html")

def add_show(request):
    return render(request, "first_app/add_show.html")

def create_show(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/new")
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        print('>>>>>>>>>>>>')
        title = request.POST["title"]
        network = request.POST["network"]
        release_date = request.POST["date"]
        print(release_date)
        description = request.POST["description"]
        new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        print(new_show)
        id = new_show.id
        messages.success(request, "Show successfully added")
        return redirect("/shows/"+str(id))

def display_show(request, my_val):
    print("*"*50)
    print(my_val)
    dict_show ={
        "show" : Show.objects.get(id=my_val)
    }
    return render(request, "first_app/show_display.html", dict_show)

def all_shows(request):
    context = {
        "show" : Show.objects.all()
    }
    return render(request, "first_app/display_show.html", context)

def edit_show(request, my_val):
    print(my_val)
    dict = {
        "show" : Show.objects.get(id=my_val)
    }
    return render(request, "first_app/edit.html", dict)

def update(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/new")
    else:
        show_id = request.POST["id"]
        print(show_id)
        title = request.POST["title"]
        network = request.POST["network"]
        release_date = request.POST["date"] 
        description = request.POST["description"]
        get_show = Show.objects.get(id=show_id)
        get_show.title  = title
        get_show.network = network
        get_show.release_date = release_date
        get_show.description = description
        get_show.save()
        messages.success(request, "Show successfully added")
        return redirect("/shows")

def delete_show(request, my_val):
    this_show = Show.objects.get(id=my_val)
    this_show.delete()
    return redirect("/shows")
# Create your views here.