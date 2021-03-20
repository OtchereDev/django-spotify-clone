from musics.models import Album, Music
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .form import AddMusicForm

def homePage(request):
    musics=list(Music.objects.all().values())
    return render(request,'home.html',{
        'musics':musics
    })

def addMusic(request):
    form=AddMusicForm()

    if request.POST:
        form=AddMusicForm(request.POST,request.FILES)
     
        if form.is_valid():
            instance=form.save(commit=False)
            album=form.cleaned_data.get('album')
            if album:
                music_album=Album.objects.get_or_create(name=album)
                print(music_album)
                instance.album=music_album[0]
                instance.save()
                return redirect("music:home_page")
            else:
                instance.save()
                return redirect("music:home_page")

        else:
            print("no",form.data)
    
    return render(request,'addPage.html',{
        'form':form
    })
