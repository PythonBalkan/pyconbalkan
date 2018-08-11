from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from pyconbalkan.contact.models import Contact
from pyconbalkan.contact.serializers import ContactSerializer
from .forms import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]


def contact_view(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send Email to info@pyconbalkan.com
            EmailMessage(
                subject='Contact Us: {}'.format(contact.name),
                body=str(contact.message),
                from_email='website@pyconbalkan.com',
                to=['info@pyconbalkan.com'],
                reply_to=[contact.email],
            ).send()
            context['success'] = 'Your message was saved successfully! '
            form = ContactForm()
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact.html', context)
