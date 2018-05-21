from django.db import models
from django import forms
from django.forms import ModelForm


class Contact(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()


class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
                           max_length=256, error_messages={'required': 'Please enter your name.'})
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}),
                              max_length=100, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                             error_messages={'required': 'Please enter a valid email address.',
                                             'invalid': 'Please enter a valid email address.'})
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}),
                              error_messages={'required': 'Please enter your message.'})

    class Meta:
        model = Contact
        fields = '__all__'
