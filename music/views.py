from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

# Create your views here.
def index(request):
	# Query all database objects,
	all_albums = Album.objects.all()
	# Assign the template for the view
	template = loader.get_template('music/index.html')
	context = {
			'all_albums': all_albums,
	}

	return HttpResponse(template.render(context,request))

def detail(request, album_id):
	return HttpResponse("<h2>Details for view " + str(album_id) +" </h2>" )