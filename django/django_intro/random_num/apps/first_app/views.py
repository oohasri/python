from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	request.session['count'] = 0
	return render(request, 'first_app/index.html')

def generate_random(request):
	request.session['count'] += 1
	print(request.session['count'])
	random_string = {
		"string": get_random_string(length=14)
	}
	print(random_string)
	return render(request, 'first_app/index.html', random_string)

def destroy(request):
	request.session.clear()
	return redirect('/')
# Create your views here.