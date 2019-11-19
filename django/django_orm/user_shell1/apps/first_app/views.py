from django.shortcuts import render
from .models import User

def index(request):
    context = {
    	"all_the_users": User.objects.all()
    }
    return render(request, "first_app/index.html", context)
# Create your views here.

# Create your views here.
