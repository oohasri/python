from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
import datetime
from datetime import timezone, tzinfo

def index(request):
	return render(request, "login/index.html")

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
				last_name=request.POST["last_name"],
				birthday=request.POST["age"],
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
			'messages' : Message.objects.all().order_by("-created_at"),
			'comments' : Comment.objects.all(),
			'time_check' : datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(seconds=60 * 30),
		}
		
		return render(request, "login/wall.html", dict)
	else:
		return render(request, "login/index.html") 

def success(request):
	if 'userid' in request.session:
		return redirect("/wall")
	else:
		return render(request, "login/index.html")  
	# return render(request, "login/success.html")

def post_submit(request):
	errors = User.objects.post_validator(request.POST)
	if len(errors) > 0:
		for key,value in errors.items():
			messages.error(request, value)
		return redirect("/wall")
	else:
		if 'userid' in request.session:
			print(request.session['userid'])
			user = User.objects.filter(id = request.session["userid"])
			print(user.values())
			if user:
				Message.objects.create(user=user[0], message=request.POST["content"])
				return redirect("/wall")

def post_comment(request):
	if 'userid' in request.session:
		this_message = request.POST["message_id"]
		print(this_message)
		this_comment = request.POST["post"]
		print(this_comment)
		this_user = Message.objects.filter(id=this_message)
		Comment.objects.create(message_id = this_user[0] ,user_id= this_user[0].user ,comment= this_comment)
		return redirect("/wall")
	else: 
		return render(request, "login/index.html")  

def message_delete(request):
	if 'userid' in request.session:
		this_message = request.POST["message"]
		message_delete = Message.objects.filter(id=this_message)
		print(message_delete[0].user.id)
		print(request.session["userid"])
		if message_delete[0].user.id == request.session["userid"]:
			message_delete[0].delete()
			return redirect("/wall")
	else:
		pass

def destroy(request):
	request.session.flush()
	return redirect("/")
# Create your views here.
