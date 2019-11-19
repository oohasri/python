from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print("context")
    return render(request,'first_app/index.html', context)


# Create your views here.
