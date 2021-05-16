from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import get_list_or_404, render
from rest_framework import generics
from rest_framework.response import Response
from ..models import AudioBook, Podcast, Podcast_Participants, Song
from django.shortcuts import get_object_or_404
from .serializers import PodcastParticipantsSerializer, SongSerializer, PodcastSerializer, AudioBookSerializer
from django.views.generic.edit import DeleteView


# Create your views here.
def AudioFiles(request):
    return render(request, "Home.html")


class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongUpdateView(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.NameOfSong = request.data.get("NameOfSong")
        return super().update(request, *args, **kwargs)


class SongDeleteView(DeleteView):
    model = Song
    success_url = "/api/songs"


class PodcastView(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class PodcastUpdateView(generics.UpdateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.NameOfPodcast = request.data.get("NameOfPodcast")
        return super().update(request, *args, **kwargs)


class PodcastDeleteView(DeleteView):
    model = Podcast
    success_url = "/api/podcasts"


class PodcastParticipantsView(generics.ListCreateAPIView):
    queryset = Podcast_Participants.objects.all()
    serializer_class = PodcastParticipantsSerializer

    def get(self, request, pk, *args, **kwargs):
        party = Podcast_Participants.objects.filter(podcast_id=pk)
        participants_list = []
        for i in party:
            print(i)
            serialized_data = PodcastParticipantsSerializer(i).data
            participants_list.append(serialized_data)
        return Response(participants_list)


class PodcastParticipantsUpdateView(generics.UpdateAPIView):
    queryset = Podcast_Participants.objects.all()
    serializer_class = PodcastParticipantsSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.participants = request.data.get("participants")
        return super().update(request, *args, **kwargs)


class PodcastParticipantsDeleteView(DeleteView):
    model = Podcast_Participants
    success_url = "/api/podcasts/"


class AudioBookView(generics.ListCreateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer


class AudioBookUpdateView(generics.UpdateAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.TitleOfAudioBook = request.data.get("TitleOfAudioBook")
        return super().update(request, *args, **kwargs)


class AudioBookDeleteView(DeleteView):
    model = AudioBook
    success_url = "/api/audiobooks"
