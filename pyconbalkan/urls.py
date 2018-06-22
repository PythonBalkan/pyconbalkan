from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve

from pyconbalkan.cfp.views import cfp_view
from pyconbalkan.conference.api_urls import router as conference
from pyconbalkan.core import routers, views
from pyconbalkan.about.views import about_view
from pyconbalkan.sponsors.views import sponsors_view
from pyconbalkan.contact.views import contact_view
from pyconbalkan.news.views import *
from pyconbalkan.speaker.views import *
from pyconbalkan.organizers.views import organizer_view, organizers_listview
from pyconbalkan.settings import PDF_ROOT
from pyconbalkan.organizers.api_urls import router as organizers
from pyconbalkan.speaker.api_urls import router as speaker
from pyconbalkan.about.api_urls import router as about
from pyconbalkan.sponsors.api_urls import router as sponsors
from pyconbalkan.cfp.api_urls import router as cfp
from pyconbalkan.contact.api_urls import router as contact
from pyconbalkan.news.api_urls import router as news
from pyconbalkan.timetable.views import timetable_view

from markdownx import urls as markdownx

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
    path('speaker/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('organizers/<slug:slug>/', organizer_view, name='organizer_detail'),
    path('organizers', organizers_listview, name='organizers'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('cfp', cfp_view, name='cfp'),
    path('news', news_view, name='news'),
    path('news/<slug:slug>/', post_detail, name='post_detail'),
    path('coc', serve, {'path': 'coc_pyconbalkan.pdf', 'document_root': PDF_ROOT}),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API
    path('markdownx/', include(markdownx)),
    path('timetable/', timetable_view, name='timetable')
]
