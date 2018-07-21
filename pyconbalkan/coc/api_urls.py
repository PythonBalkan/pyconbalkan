from rest_framework import routers
from .views import CodeOfConductViewSet

router = routers.DefaultRouter()
router.register(r'coc', CodeOfConductViewSet)
