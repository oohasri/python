from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages

def index(request):
	return render(request, "book/index.html")

def register(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key,value in errors.items():
			messages.error(request, value)
		return redirect("/")
	else:
		user_check = User.objects.filter(email=request.POST["email"])
		if not user_check:
			password = request.POST["password"]
			pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # create the hash    
			print(pw_hash)      
			user = User.objects.create(first_name=request.POST["first_name"],
				alias=request.POST["alias"],
				email=request.POST["email"],
				password=pw_hash)
			request.session['userid'] = user.id
			request.session['first_name'] = user.first_name
			return redirect("/login_success")
		else:
			errors["user_exists"] = "User already exists"
			if len(errors) > 0:
				for key,value in errors.items():
					messages.error(request, value)
				return redirect("/")

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors) > 0:
		for key,value in errors.items():
			messages.error(request, value)
		return redirect("/")
	else:
		username = request.POST['email']
		password = request.POST['password']
		user = User.objects.filter(email=request.POST["email"])
		if user:
			logged_user = user[0]
			if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
				request.session['userid'] = logged_user.id
				request.session['first_name'] = logged_user.first_name
				return redirect('/login_success')
		return redirect("/")

def user_wall(request):
	if 'userid' in request.session:
		dict= {
			'books' : Book.objects.all().order_by("-created_at"),
			'reviews' :Review.objects.all().order_by("-created_at")[:3],
		}		
		return render(request, "book/wall.html", dict)
	else:
		return render(request, "book/index.html")

def add_book(request):
	if 'userid' in request.session:
		dict= {
			'authors' : Author.objects.all(),
		}		
		return render(request, "book/addbook.html", dict)
	else:
		return render(request, "book/index.html")

def book_post(request):
	if 'userid' in request.session:
		this_book = Book.objects.all()
		print(request.POST)
		print(request.POST["author"])
		for book in this_book:
			if book.title == request.POST["title"]:
				dict = {
					'message_update' : "Book already exists! Please add a new book",
					'authors' : Author.objects.all(),
				}
				return render(request, "book/addbook.html", dict)
		this_author = Author.objects.filter(author_name=request.POST["author"])
		if not this_author:
			new_author = Author.objects.create(author_name=request.POST["author"])
			this_author[0] = new_author
		this_user = User.objects.filter(id=request.session["userid"])
		book = Book.objects.create(title=request.POST["title"], user=this_user[0], author=this_author[0])
		Review.objects.create(review=request.POST["review"], rating=request.POST["rating"], user=this_user[0], book=book)			
		request.session["book_id"] = book.id
		return redirect("/display_book")
	else:
		return render(request, "book/index.html")

def success(request):
	if 'userid' in request.session:
		return redirect("/wall")
	else:
		return render(request, "book/index.html")  

def book_display(request):
	if 'userid' in request.session:
		dict = {
			'this_book' : Book.objects.filter(id=request.session["book_id"]),
			'this_review' : Review.objects.all(),
		}
		return render(request, "book/display_book.html", dict)
	else:
		return render(request, "book/index.html")  

def review_submit(request):
	if 'userid' in request.session:
		print(f"*************{request.POST['book_id']}")
		this_user = User.objects.filter(id=request.session["userid"])
		this_book = Book.objects.filter(id=request.POST["book_id"])
		Review.objects.create(review=request.POST["review"], rating=request.POST["rating"], user=this_user[0], book=this_book[0])
		return redirect("/display_book")
	else:
		return render(request, "book/index.html")  

def destroy(request):
	request.session.flush()
	return redirect("/")

# Create your views here.
