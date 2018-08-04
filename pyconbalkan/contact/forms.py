from django import forms
from django.forms import ModelForm

from pyconbalkan.contact.models import Contact


class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
                           max_length=256, error_messages={'required': 'Please, enter your name.'}, label='')
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company', 'class': 'form-control'}),
                              max_length=100, required=False, label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                             error_messages={'required': 'Please, enter a valid email address.',
                                             'invalid': 'Please enter a valid email address.'}, label='')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}),
                              error_messages={'required': 'Please, enter your message.'}, label='')

    class Meta:
        model = Contact
        fields = '__all__'