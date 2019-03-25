from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            contact = form.save()
            # Send Email to info@pyconbalkan.com
            EmailMessage(
                subject='Contact Us: {}'.format(contact.name),
                body=str(contact.message),
                from_email='website@pyconbalkan.com',
                to=['info@pyconbalkan.com'],
                reply_to=[contact.email],
            ).send()
            return HttpResponseRedirect(reverse("contact_success"))

    context = {
        'form': form,
        "RECAPTCHA_SECRET_KEY": settings.RECAPTCHA_SECRET_KEY,
    }
    return render(request, "contact_form/contact.html", context)
