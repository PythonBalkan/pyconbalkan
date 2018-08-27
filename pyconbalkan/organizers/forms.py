from django import forms
from django.db import transaction

from pyconbalkan.organizers.models import Volunteer, VolunteerPhoto


class VolunteerCreateForm(forms.ModelForm):
    required_fields = (
        'full_name', 'name', 'date_of_birth', 'job',
        'email', 'description', 'country', 'profile_photo'
    )

    profile_picture = forms.ImageField(label='Profile Photo', required=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for name, field in self.fields.items():
            self.add_required(name, field)
            self.add_form_control(field)
            self.label_as_placeholder(field, name)

    def add_form_control(self, field):
        old_classes = field.widget.attrs['class'] if 'class' in field.widget.attrs else ''
        field.widget.attrs.update({'class': f'{old_classes} form-control'})

    def label_as_placeholder(self, field, name):
        placeholder = field.label if not field.required else field.label + '*'
        field.widget.attrs.update({'placeholder': placeholder})

        if name != 'profile_picture':
            field.label = ''
        else:
            field.label = placeholder

    def add_required(self, name, field):
        if name in self.required_fields:
            field.required = True

    def save(self, commit=True):
        """
        Save both Volunteer model and VolunteerPhoto at once.
        If more complex - maybe add formset.
        """

        with transaction.atomic():
            instance = super().save(commit=commit)
            VolunteerPhoto.objects.create(
                volunteer=instance, profile_picture=self.cleaned_data['profile_picture']
            )
        return instance

    class Meta:
        model = Volunteer
        exclude = ('active', 'user', 'type', 'slug', )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'}),
        }
