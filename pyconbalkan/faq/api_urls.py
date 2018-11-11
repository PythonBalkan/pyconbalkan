from rest_framework import routers

from pyconbalkan.faq.views import FaqViewSet

router = routers.DefaultRouter()
router.register(r'faq', FaqViewSet)
