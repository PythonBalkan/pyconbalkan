import random
import string

from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect
from markdownx.models import MarkdownxField
from slugify import slugify

TALK = 1
WORKSHOP = 2
TYPE_CFP = (
    (TALK, 'Talk'),
    (WORKSHOP, 'Workshop'),
)

class Cfp(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    personal_website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    description = MarkdownxField()
    accepted = models.BooleanField(default=False)
    slug = models.CharField(unique=True, blank=True, max_length=100)
    type = models.IntegerField(choices=TYPE_CFP, default=TALK)
    duration = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{}: "{}" by {} - [{}]'.format(self.get_type_display(), self.title, self.name, 'Accepted' if self.accepted else 'Pending')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('{}-{}'.format(self.name, self.title))
            if Cfp.objects.filter(slug=self.slug):
                self.slug = '{}-{}-{}'.format(slugify(self.name), slugify(self.title), ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)))
        super(Cfp, self).save(*args, **kwargs)


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
    type = forms.ChoiceField(choices=TYPE_CFP, widget=RadioSelect())

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