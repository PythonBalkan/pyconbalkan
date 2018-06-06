from django.db import models
from django import forms
from django.forms import ModelForm
from markdownx.models import MarkdownxField


class Cfp(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    personal_website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    description = MarkdownxField()



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
                              error_messages={'required': 'Please, enter your message.'}, label='')
    description= forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description of your proposal', 'class': 'form-control'}),
                              error_messages={'required': 'Please, enter your message.'}, label='')

    class Meta:
        model = Cfp
        fields = '__all__'