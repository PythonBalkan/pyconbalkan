from rest_framework import routers
from pyconbalkan.contact.views import ContactViewSet


router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)
