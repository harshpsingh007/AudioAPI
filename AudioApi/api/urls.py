from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.AudioFiles, name="AudioFiles"),
    path('songs/', views.SongView.as_view(), name="SongView"),
    path('songs/update/<pk>/', views.SongUpdateView.as_view(), name="SongUpdateView"),
    path('songs/delete/<pk>/', views.SongDeleteView.as_view(), name="SongDeleteView"),
    path('podcasts/', views.PodcastView.as_view(), name="PodcastView"),
    path('podcasts/update/<pk>', views.PodcastUpdateView.as_view(), name="PodcastUpdateView"),
    path('podcasts/delete/<pk>', views.PodcastDeleteView.as_view(), name="PodcastDeleteView"),
    path('podcasts/<pk>/participants', views.PodcastParticipantsView.as_view(), name="PodcastParticipantsView"),
    path('podcasts/participants/update/<podcast_id>/<pk>', views.PodcastParticipantsUpdateView.as_view(), name="PodcastParticipantsUpdateView"),
    path('podcasts/participants/delete/<podcast_id>/<pk>', views.PodcastParticipantsDeleteView.as_view(), name="PodcastParticipantsDeleteView"),
    path('audiobooks/', views.AudioBookView.as_view(), name="AudioBookView"),
    path('audiobooks/update/<pk>', views.AudioBookUpdateView.as_view(), name="AudioBookUpdateView"),
    path('audiobooks/delete/<pk>', views.AudioBookDeleteView.as_view(), name="AudioBookDeleteView"),
]
