from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from markdownx import urls as markdownx

from pyconbalkan.cfp.views import cfp_view
from pyconbalkan.conference.api_urls import router as conference
from pyconbalkan.core import routers, views
from pyconbalkan.about.views import about_view
from pyconbalkan.contact.views import contact_view
from pyconbalkan.news.views import *
from pyconbalkan.organizers.views import organizers_view
from pyconbalkan.settings import PDF_ROOT
from pyconbalkan.organizers.api_urls import router as organizers
from pyconbalkan.speaker.api_urls import router as speaker
from pyconbalkan.about.api_urls import router as about
from pyconbalkan.sponsors.api_urls import router as sponsors
from pyconbalkan.cfp.api_urls import router as cfp
from pyconbalkan.contact.api_urls import router as contact
from pyconbalkan.news.api_urls import router as news


router = routers.DefaultRouter()
router.extend(conference)
router.extend(speaker)
router.extend(organizers)
router.extend(about)
router.extend(contact)
router.extend(sponsors)
router.extend(cfp)
router.extend(contact)
router.extend(news)

urlpatterns = [
    path('', views.home, name='index'),
    path('organizers', organizers_view, name='organizers'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('cfp', cfp_view, name='cfp'),
    path('news', news_view, name='news'),
    path('news/<slug:pk>/', post_detail, name='post_detail'),
    path('coc', serve, {'path': 'coc_pyconbalkan.pdf', 'document_root': PDF_ROOT}),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API
    path('markdownx/', include(markdownx)),
]
