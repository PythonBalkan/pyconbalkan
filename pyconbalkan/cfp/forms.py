from django import forms
from django.conf import settings
from django.forms import ModelForm

from pyconbalkan.cfp.models import CFPRating
from .models import Cfp
from . import const


class CfpForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
                           max_length=256, error_messages={'required': 'Please, enter your name.'}, label='')
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}),
                              max_length=100, required=False, label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                             error_messages={'required': 'Please, enter a valid email address.',
                                             'invalid': 'Please enter a valid email address.'}, label='')
    personal_website = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Personal Website (URL)', 'class': 'form-control'}),
                                       max_length=100, required=False, label='')
    linkedin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Linkedin (URL)', 'class': 'form-control'}),
                               max_length=100, required=False, label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title of your proposal', 'class': 'form-control'}),
                            error_messages={'required': 'Please, enter the title.'}, label='')
    duration = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Duration (E.g. 2h, 30min, 1:30, etc.)', 'class': 'form-control'}),
                               error_messages={'required': 'Please, enter the duration.'}, label='')
    description= forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description of your proposal', 'class': 'form-control'}),
                              error_messages={'required': 'Please, enter the description of your proposal.'}, label='')
    type = forms.ChoiceField(choices=const.TYPE_CFP, widget=forms.Select())

    class Meta:
        model = Cfp
        fields = (
            'name',
            'company',
            'email',
            'personal_website',
            'linkedin',
            'title',
            'duration',
            'description',
            'type',
        )


class RateForm(ModelForm):
    class Meta:
        model = CFPRating
        fields = (
            'mark',
        )