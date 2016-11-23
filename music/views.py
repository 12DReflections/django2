from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse("<h1>This is a music website</h1>")

def detail(request, album_id):
	return HttpResponse("<h2>Details for view</h2>" + str(album_id))