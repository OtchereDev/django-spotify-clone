from django.forms import widgets
from musics.models import Music
from django import forms

class AddMusicForm(forms.ModelForm):
    album=forms.CharField(max_length=500,required=False)
    
    class Meta:
        model=Music
        fields=[
            'title',
            'artiste',
           
            'audio_file',
            'cover_image',
        ]
