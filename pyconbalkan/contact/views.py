from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from pyconbalkan.contact.serializers import ContactSerializer
from pyconbalkan.contact.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]
