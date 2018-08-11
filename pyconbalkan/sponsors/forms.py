from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect

from pyconbalkan.sponsors.models import Sponsoring, ORGANIZATION_CHOICES, SponsorshipLevel


class SponsoringForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
        max_length=256,
        error_messages={'required': 'Please, enter your name.'}, label='')
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'form-control'}),
        max_length=17,
        error_messages={
            'required': 'Please, enter your phone number.',
            'invalid': 'Please, enter a valid phone number.'
        }, label='')
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        error_messages={
            'required': 'Please, enter your email address.',
            'invalid': 'Please, enter a valid email address.'
        }, label='')
    organization = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Company / Organization', 'class': 'form-control'}),
        max_length=100,
        required=False, label='')
    organization_type = forms.ChoiceField(choices=ORGANIZATION_CHOICES, label='Organization Type', widget=RadioSelect())
    level = forms.ChoiceField(choices=SponsorshipLevel.choices, label='Level of Interest', widget=RadioSelect())

    class Meta:
        model = Sponsoring
        fields = (
            'name',
            'phone',
            'email',
            'organization',
            'organization_type',
            'level'
        )
