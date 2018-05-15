from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from pyconbalkan.conference.api_urls import router as conference
from pyconbalkan.core import routers, views
from pyconbalkan.about.views import about_view
from pyconbalkan.organizers.views import organizers_view
from pyconbalkan.settings import PDF_ROOT
from pyconbalkan.organizers.api_urls import router as organizers
from pyconbalkan.speaker.api_urls import router as speaker
from pyconbalkan.about.api_urls import router as about
from pyconbalkan.sponsors.api_urls import router as sponsors
from pyconbalkan.cfp.api_urls import router as cfp

router = routers.DefaultRouter()
router.extend(conference)
router.extend(speaker)
router.extend(organizers)
router.extend(about)
router.extend(sponsors)
router.extend(cfp)

urlpatterns = [
    path('', views.home, name='index'),
    path('organizers', organizers_view, name='organizers'),
    path('about', about_view, name='about'),
    path('coc', serve, {'path': 'coc_pyconbalkan.pdf', 'document_root': PDF_ROOT}),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # API
]
