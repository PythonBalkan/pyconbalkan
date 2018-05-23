from django.shortcuts import render
from rest_framework import viewsets
from pyconbalkan.cfp.models import Cfp, CfpForm
from pyconbalkan.cfp.serializers import CfpSerializer
from pyconbalkan.conference.models import Conference


class CfpViewSet(viewsets.ModelViewSet):
    queryset = Cfp.objects.all()
    serializer_class = CfpSerializer


def cfp_view(request):
    conference = Conference.objects.filter(active=True)
    context = {
        'conference': conference.first() if conference else None,
    }
    if request.method == 'POST':
        form = CfpForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = 'Your proposal was saved successfully!'
            form = CfpForm()
    else:
        form = CfpForm()
    context['form'] = form
    return render(request, 'cfp.html', context)