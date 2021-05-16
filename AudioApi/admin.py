from django.contrib import admin
from .models import AudioBook, Podcast, Podcast_Participants, Song
# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id",'NameOfSong','durationOfSong','uploaded_time']
    ordering = ["id"]
    search_fields = ['NameOfSong','id']
    list_filter = ["uploaded_time"]

class ParticipantsInLine(admin.StackedInline):
    model = Podcast_Participants
    max_num = 10

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ["id","NameOfPodcast","host","durationOfPodcast","uploaded_time"]
    ordering = ['id']
    search_fields = ["id","NameOfPodcast","host"]
    inlines = [ParticipantsInLine]

@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ["id","TitleOfAudioBook","author","narrator","durationOfAudioBook","uploaded_time"]
    ordering = ['id']
    search_fields = ['TitleOfAudioBook',"author","narrator"]