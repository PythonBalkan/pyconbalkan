from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect

from pyconbalkan.sponsors.models import Sponsoring


class SponsoringForm(ModelForm):
    organization = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
        required=False,
        label='Sponsor Organization')
    organization_type = forms.ChoiceField(choices=((0, 'For - profit corporation'), (1, 'Foundation / Non profit')), label='Type of organization', widget=RadioSelect())
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=256,
        error_messages={'required': 'Please, enter your name.'},
        label='Name and Surname')
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=17,
        error_messages={
            'required': 'Please enter your phone number.',
            'invalid': 'Please enter a valid phone number.'
        },
        label='Phone number')
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Please, enter a valid email address.',
            'invalid': 'Please enter a valid email address.'
        },
        label='e-mail')
    CHOICES = (('platinum', '5000'),
               ('gold', '2500'),
               ('silver', '1000'),
               ('bronze', '500'),)
    level = forms.ChoiceField(choices=CHOICES, label='Level of sponsorship', widget=RadioSelect())

    class Meta:
        model = Sponsoring
        fields = '__all__'
