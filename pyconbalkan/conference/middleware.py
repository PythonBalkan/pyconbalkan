from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponseRedirect

from pyconbalkan.conference.models import Conference


class ConferenceSelectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Domain format : 2019.pyconbalkan.com
        domain = request.META['HTTP_HOST']
        try:
            domain_year = int(domain.split('.')[0])
            q = {
                "year": domain_year
            }
            if not request.user.is_superuser:
                q['active'] = True

            conference = Conference.objects.get(**q)
        except (Conference.DoesNotExist, ValueError):
            conference = Conference.objects.filter(active=True).first()

        conference_domain = conference.year + "." + settings.META_SITE_DOMAIN
        if conference_domain != request.META['HTTP_HOST']:
            return HttpResponseRedirect(
                urljoin()
            )

        # Every request will have an atribute `conference` in it
        # `conference` is the conference.models.Conference object for the
        # respective year fetched from it's domain
        request.conference = conference
        response = self.get_response(request)
        return response
