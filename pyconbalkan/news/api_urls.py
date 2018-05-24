from rest_framework import routers
from pyconbalkan.news.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'news', PostViewSet)
