from rest_framework import routers

from pyconbalkan.conference.views import ConferenceViewSet

router = routers.DefaultRouter()
router.register(r'conference', ConferenceViewSet)