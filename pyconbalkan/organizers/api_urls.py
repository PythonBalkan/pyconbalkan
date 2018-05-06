from rest_framework import routers

from pyconbalkan.organizers.views import VolunteerViewSet

router = routers.DefaultRouter()
router.register(r'organizers', VolunteerViewSet)