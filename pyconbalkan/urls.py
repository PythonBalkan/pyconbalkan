from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from pyconbalkan.conference.api_urls import router as conference
from pyconbalkan.core import routers, views
from pyconbalkan.organizers.api_urls import router as organizers
from pyconbalkan.settings import PDF_ROOT
from pyconbalkan.speaker.api_urls import router as speaker

router = routers.DefaultRouter()
router.extend(conference)
router.extend(speaker)
router.extend(organizers)

urlpatterns = [
    path('', views.home, name='index'),
    path('organizers', views.organizers, name='organizers'),
    path('coc', serve, {'path': 'coc_pyconbalkan.pdf', 'document_root': PDF_ROOT}),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # API
]