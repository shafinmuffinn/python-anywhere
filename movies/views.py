from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "movies/index.html")