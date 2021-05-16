from django.db.models import fields
from ..models import AudioBook, Podcast, Podcast_Participants, Song
from rest_framework import serializers
from ..admin import ParticipantsInLine

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ["id",'NameOfSong','durationOfSong','uploaded_time']

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ["id",'NameOfPodcast','durationOfPodcast','uploaded_time',"host"]

class PodcastParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast_Participants
        fields = ["id","podcast","participants"]

class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ["id",'TitleOfAudioBook','author','narrator','durationOfAudioBook','uploaded_time']