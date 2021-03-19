from musics.models import Music
from django.shortcuts import render
from django.http import JsonResponse

def homePage(request):
    return render(request,'home.html')

def musicList(request):
    music=Music.objects.all().values()
    return JsonResponse(list(music),safe=False)
