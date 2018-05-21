from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from pyconbalkan.contact.serializers import ContactSerializer
from pyconbalkan.contact.models import Contact
from django.shortcuts import render
from .models import ContactForm


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
