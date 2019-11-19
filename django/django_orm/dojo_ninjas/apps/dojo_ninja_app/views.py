from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
	return render(request, "dojo_ninja_app/index.html")

def template(request):
	books = {
		"books" : Book.objects.all()
	}
	return render(request, "dojo_ninja_app/template.html", books)

def authors_template(request):
	authors = {
		"authors" : Author.objects.all()
	}
	return render(request, "dojo_ninja_app/authors_template.html", authors)

def addbook(request):
	title = request.POST["title"]
	print(title)
	desc = request.POST["description"]
	Book.objects.create(title=title, desc=desc)
	return redirect("/books_template")

def display_book(request, my_val):
	print(my_val)
	books = Book.objects.get(id=my_val)
	authors = books.authors.values()
	all_authors = Author.objects.all()
	print(authors)
	dict = {
		"book" : books,
		"authors" : authors,
		"all_authors" : all_authors
	}
	return render(request, "dojo_ninja_app/display_book.html", dict)

def add_new_author(request):
	print("abc"*40)
	add_author = request.POST["select_authors"]
	this_book = request.POST["property"]
	get_book = Book.objects.get(id=this_book)
	get_author = Author.objects.get(id=add_author)
	get_book.authors.add(get_author)
	return redirect("/book/"+this_book)

def addauthor(request):
	first_name = request.POST["first_name"]
	last_name = request.POST["last_name"]
	notes = request.POST["notes"]
	Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
	return redirect("/authors_template")

def display_author(request, my_val):
	authors = Author.objects.get(id=my_val)
	books = authors.books.values()
	all_books = Book.objects.all()
	print("eee"*50)
	print(books)
	dict = {
		"books" : books,
		"author" : authors,
		"all_books" : all_books
	}
	return render(request, "dojo_ninja_app/display_author.html", dict)

def add_new_book(request):
	print("abc"*40)
	add_book = request.POST["select_books"]
	this_author = request.POST["property"]
	get_author = Author.objects.get(id=this_author)
	get_book = Book.objects.get(id=add_book)
	get_author.books.add(get_book)
	return redirect("/author/"+this_author)

# Create your views here.
