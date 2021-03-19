from musics.views import homePage, musicList
from django.urls import path

app_name='musics'

urlpatterns = [
    path('',homePage,name='home_page'),
    path('list/',musicList,name='music_list'),    
]
