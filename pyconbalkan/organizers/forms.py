from django import forms

from pyconbalkan.organizers.models import Volunteer


class VolunteerCreateForm(forms.ModelForm):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # delete labels, add form-control class to all fields
        for f in self.fields.values():
            old_classes = f.widget.attrs['class'] if 'class' in f.widget.attrs else ''
            f.widget.attrs.update({'placeholder': f.label, 'class': f'{old_classes} form-control'})
            f.label = ''

    class Meta:
        model = Volunteer
        exclude = ('active', 'user', 'weight', 'type', 'slug', 'description', )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'}),
        }
