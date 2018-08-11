from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.db.models import Subquery, OuterRef
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from pyconbalkan.cfp.forms import CfpForm, RateForm
from pyconbalkan.cfp.models import Cfp, CFPRating
from pyconbalkan.cfp.serializers import CfpSerializer


class CfpViewSet(viewsets.ModelViewSet):
    queryset = Cfp.objects.all()
    serializer_class = CfpSerializer
    permission_classes = (DjangoModelPermissions,)


def cfp_view(request):
    context = {}
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
    cfps = Cfp.objects.annotate(
        my_rating=Subquery(CFPRating.objects.filter(cfp=OuterRef('pk'), user=request.user).values('mark'))
    )

    context = {
        'cfps': cfps,
    }
    return render(request, 'cfp_list.html', context)


@login_required
def cfp_detail(request, slug):
    cfp = get_object_or_404(Cfp, slug=slug)
    ratings = CFPRating.objects.filter(cfp=cfp)
    context = {
        'cfp': cfp,
        'ratings': ratings,
    }
    initial = {
        'user': request.user,
        'cfp': cfp
    }
    try:
        rating_instance = CFPRating.objects.get(**initial)
    except CFPRating.DoesNotExist:
        rating_instance = CFPRating(**initial)
    if request.method == 'POST':
        form = RateForm(request.POST, instance=rating_instance)
        if form.is_valid():
            form.save()
            context['success'] = 'Your review has been successfully saved.'
    else:
        form = RateForm(instance=rating_instance)
    context['form'] = form
    return render(request, 'cfp_detail.html', context)