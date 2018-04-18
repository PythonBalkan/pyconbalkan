from django.shortcuts import render
from .models import Speaker, SpeakerPhoto


def home(request):
    speaker = Speaker.objects.all()
    speakerPh = SpeakerPhoto.objects.all()
    context = {'speakers': speaker, 'speakerPhoto': speakerPh}
    return render(request, 'index.html', context)


