from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from pyconbalkan.core import views, routers
from pyconbalkan.settings import PDF_ROOT
from pyconbalkan.conference.api_urls import router as conference
from pyconbalkan.speaker.api_urls import router as speaker
from pyconbalkan.organizers.api_urls import router as organizers


router = routers.DefaultRouter()
router.extend(conference)
router.extend(speaker)
router.extend(organizers)

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^cfp$', views.cfp, name='cfp'),
    url(r'^sponsors$', views.sponsors, name='sponsors'),
    url(r'^organizers$', views.organizers, name='organizers'),
    url(r'^coc$', serve, {'path': 'coc_pyconbalkan.pdf', 'document_root': PDF_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),  # API
]
