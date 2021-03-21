from musics.views import addMusic, homePage
from django.urls import path

app_name='musics'

urlpatterns = [
    path('',homePage,name='home_page'), 
    path('add/',addMusic,name='add_music'),  
]
