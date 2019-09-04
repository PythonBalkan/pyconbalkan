import datetime

from django import forms
from django.forms import ModelMultipleChoiceField, ChoiceField
from django_select2.forms import Select2Widget, ModelSelect2Widget

from pyconbalkan.conference.models import Conference
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.sponsors.models import Sponsor


class SpeakerForm(forms.Form):
    pk = forms.ChoiceField(
        label="",
        widget=ModelSelect2Widget(
            model=Speaker,
            search_fields=['full_name__icontains'],
            max_results=15
        )
    )

    class Media:
        js = (
            'js/search_people.js',
        )


def previous_conferences(request):
    return {
        'sidebar_sponsors': Sponsor.objects.filter(sidebar=True, active=True),
        'current_conferences': Conference.objects.filter(year__lte=datetime.datetime.now().year),
        'previous_conferences': Conference.objects.filter(year__lt=datetime.datetime.now().year),
        'search_speakers': SpeakerForm()
    }