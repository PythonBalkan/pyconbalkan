from pyconbalkan.conference.models import Conference


class ConferenceSelectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Domain format : 2019.pyconbalkan.com
        domain = request.META['HTTP_HOST']
        conference = Conference.objects.get(year=domain.split('.')[0])
        # Every request will have an atribute `conference` in it
        # `conference` is the conference.models.Conference object for the
        # respective year fetched from it's domain
        request.conference = conference
        response = self.get_response(request)
        return response
