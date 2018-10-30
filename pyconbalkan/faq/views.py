from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.faq.models import Faq
from pyconbalkan.faq.serializers import FaqSerializer
from pyconbalkan.coc.views import coc_view
from pyconbalkan.organizers.views import organizers_list


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


def faq_view(request):
    faq = Faq.objects.filter(active=True)
    context = {
        'faq': faq,
    }
    return render(request, 'faq.html', context)
