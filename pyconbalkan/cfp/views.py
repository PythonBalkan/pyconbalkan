from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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
            cfp = form.save()
            body = '{}'.format(cfp.description)
            # Send Email to info@pyconbalkan.com
            EmailMessage(
                subject='CFP: {} by {}'.format(cfp.title, cfp.name),
                body=str(body),
                from_email='website@pyconbalkan.com',
                to=['cfp@pyconbalkan.com'],
                reply_to=[cfp.email],
            ).send()
            context['success'] = 'Your proposal was saved successfully!'
            form = CfpForm()
    else:
        form = CfpForm()
    context['form'] = form
    return render(request, 'cfp_form.html', context)


@login_required
def cfp_list(request):
    cfps = Cfp.objects.all()
    context = {
        'cfps': cfps,
    }
    return render(request, 'cfp_list.html', context)


@login_required
def cfp_detail(request, slug):
    cfp = get_object_or_404(Cfp, slug=slug)
    context = {
        'cfp': cfp,
    }
    return render(request, 'cfp_detail.html', context)