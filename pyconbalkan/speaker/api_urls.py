from rest_framework import routers

from pyconbalkan.speaker.views import SpeakerViewSet

router = routers.DefaultRouter()
router.register(r'speaker', SpeakerViewSet)