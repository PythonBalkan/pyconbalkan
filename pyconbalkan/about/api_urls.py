from rest_framework import routers

from pyconbalkan.about.views import AboutViewSet

router = routers.DefaultRouter()
router.register(r'about', AboutViewSet)