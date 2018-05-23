from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from pyconbalkan.conference.models import Conference
from pyconbalkan.contact.serializers import ContactSerializer
from pyconbalkan.contact.models import Contact
from django.shortcuts import render
from .models import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]


def contact_view(request):
    conference = Conference.objects.filter(active=True)
    context = {
        'conference': conference.first() if conference else None,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = 'Your message was saved successfully! '
            form = ContactForm()
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)
