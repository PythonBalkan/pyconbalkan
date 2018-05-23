from rest_framework import routers
from pyconbalkan.cfp.views import CfpViewSet

router = routers.DefaultRouter()
router.register(r'cfp', CfpViewSet)
