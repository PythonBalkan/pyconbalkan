from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponseRedirect

from pyconbalkan.conference.models import Conference


class ConferenceSelectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before
        the view (and later middleware) are called.
        Domain format : 2019.pyconbalkan.com

        Every request will have an atribute `conference` in it
        `conference` is the conference.models.Conference object for the
        respective year fetched from it's domain.
        """

        domain = request.META.get('HTTP_HOST', 'localhost')
        try:
            domain_year = int(domain.split('.')[0])
            q = {
                "year": domain_year
            }
            if not request.user.is_superuser:
                q['active'] = True

            request.conference = Conference.objects.get(**q)
        except (Conference.DoesNotExist, ValueError):
            request.conference = Conference.objects.filter(active=True).first()

        conference_domain = "{}.{}".format(
            request.conference.year,
            settings.META_SITE_DOMAIN
        )

        if settings.DEBUG is False and conference_domain != request.META['HTTP_HOST']:
            return HttpResponseRedirect(
                urljoin(
                    "{}://{}".format(settings.META_SITE_PROTOCOL, conference_domain
                ), "/")
            )

        return self.get_response(request)
