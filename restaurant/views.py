from django.shortcuts import render

# Create your views here.

def index(request):
    "This function is just for return the index web page"
    return render(request, 'index.html', {})
