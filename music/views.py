from django.http import Http404
from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
	# Query all database objects,
	all_albums = Album.objects.all()
				# request  	template			context
	return render(request, 'music/index.html', {'all_albums': all_albums })

# Get a single album
def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album could not be found")
	return render(request, 'music/detail.html', {'album': album })