from rest_framework import routers
from pyconbalkan.sponsors.views import SponsorsViewSet

router = routers.DefaultRouter()
router.register(r'sponsors', SponsorsViewSet)
