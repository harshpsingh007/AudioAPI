from django.db import models
from django.db.models.query import FlatValuesListIterable

# Create your models here.
class Song(models.Model):
    id = models.AutoField(auto_created=True,verbose_name="ID",serialize=False,primary_key=True)
    NameOfSong = models.CharField(blank=False,null=False,max_length=100)
    durationOfSong = models.IntegerField(blank=False,null=False,help_text="Time In Seconds")
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NameOfSong

class Podcast(models.Model):
    id = models.AutoField(auto_created=True,verbose_name="ID",serialize=False,primary_key=True)
    NameOfPodcast = models.CharField(blank=False,null=False,max_length=100)
    durationOfPodcast = models.IntegerField(blank=False,null=False,help_text="Time In Seconds")
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.NameOfPodcast

class Podcast_Participants(models.Model):
    podcast = models.ForeignKey(Podcast,related_name="Podcast",on_delete=models.CASCADE)
    participants = models.CharField(blank=True,null=True,max_length=100)

    def __str__(self):
        return self.participants

class AudioBook(models.Model):
    id = models.AutoField(auto_created=True,verbose_name="ID",serialize=False,primary_key=True)
    TitleOfAudioBook = models.CharField(blank=False,max_length=100)
    author = models.CharField(blank=False,max_length=100)
    narrator = models.CharField(blank=False,max_length=100)
    durationOfAudioBook = models.IntegerField(blank=False,null=False,help_text="Time In Seconds")
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TitleOfAudioBook