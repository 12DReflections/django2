from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=120)
	album_title = models.CharField(max_length=200)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

	def __str__(self):
		return self.album_title + ' - ' + self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE) # When deleting an album delete the songs
	file_type = models.CharField(max_length=100)
	song_title = models.CharField(max_length=250)

	def __str__(self):
		return self.song_title
