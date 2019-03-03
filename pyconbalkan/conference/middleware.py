from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponseRedirect

from .context import singleton
from pyconbalkan.conference.models import Conference


class ConferenceSelectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def _get_year_from_domain(self, request):
        domain = request.META.get('HTTP_HOST', 'localhost')
        try:
            return int(domain.split('.')[0])
        except ValueError:
            # Adding a non existing year, so it will never find this one, and will default to current.
            return 9999

    def __call__(self, request):
        """
        Code to be executed for each request before
        the view (and later middleware) are called.
        Domain format : 2019.pyconbalkan.com

        Every request will have an atribute `conference` in it
        `conference` is the conference.models.Conference object for the
        respective year fetched from it's domain.
        """
        if 'year' in request.GET.keys():
            domain_year = int(request.GET['year'])
        else:
            domain_year = self._get_year_from_domain(request)


        try:
            request.conference = Conference.objects.get(year=domain_year)
        except Conference.DoesNotExist:
            request.conference = Conference.objects.filter(active=True).first()
            if not request.conference:
                return self.get_response(request)

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

        # Please forgive me everyone, I couldn't find a better way of accessing the conference object globally.
        # And I really didn't want to use django.contrib.sites.models.Site
        # https://docs.djangoproject.com/en/2.1/ref/contrib/sites/#module-django.contrib.sites
        # If anyone has any better idea how to accomplish this please make a pull request.
        #
        # Idea taken from: https://stackoverflow.com/a/27694861/548059

        singleton.conference = request.conference
        return self.get_response(request)
