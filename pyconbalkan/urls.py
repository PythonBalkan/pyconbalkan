from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve
from markdownx import urls as markdownx

from pyconbalkan.about.api_urls import router as about
from pyconbalkan.about.views import about_view
from pyconbalkan.cfp.api_urls import router as cfp
from pyconbalkan.cfp.views import cfp_detail, cfp_list, cfp_view
from pyconbalkan.coc.api_urls import router as coc
from pyconbalkan.coc.views import response_guide, coc_view
from pyconbalkan.conference.api_urls import router as conference
from pyconbalkan.contact.api_urls import router as contact
from pyconbalkan.contact.views import contact_view
from pyconbalkan.core import routers, views
from pyconbalkan.info.views import info_view
from pyconbalkan.news.api_urls import router as news
from pyconbalkan.news.views import *
from pyconbalkan.organizers.api_urls import router as organizers
from pyconbalkan.organizers.views import organizer_view, volunteers_createview, organizers_list
from pyconbalkan.settings import PDF_ROOT
from pyconbalkan.speaker.api_urls import router as speaker
from pyconbalkan.speaker.views import *
from pyconbalkan.sponsors.api_urls import router as sponsors
from pyconbalkan.sponsors.views import sponsor_view, sponsoring_view, sponsors_view
from pyconbalkan.timetable.views import timetable_view
from pyconbalkan.faq.views import faq_view
from pyconbalkan.faq.api_urls import router as faq

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
router.extend(coc)
router.extend(faq)

urlpatterns = [
    path('', views.home, name='index'),
    path('speaker/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('sponsors', sponsors_view, name='sponsor_list'),
    path('speakers', speaker_list, name='speakers'),
    path('sponsors/<int:id>/', sponsor_view, name='sponsor_detail'),
    path('sponsoring', sponsoring_view, name='sponsoring'),
    path('info', info_view, name='info'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('organizers/<slug:slug>/', organizer_view, name='organizer_detail'),
    path('volunteers/create/', volunteers_createview, name='volunteers_create'),
    path('organizers', organizers_list, name='organizers'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('cfp', cfp_view, name='cfp'),
    path('cfps', cfp_list, name='cfp_list'),
    path('cfp/<slug:slug>/', cfp_detail, name='cfp_detail'),
    path('news', news_view, name='news'),
    path('news/<slug:slug>/', post_detail, name='post_detail'),
    path('coc', coc_view, name='coc'),
    path('coc/<slug:slug>/', response_guide, name='response_guide'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API
    path('markdownx/', include(markdownx)),
    path('faq', faq_view, name='faq')
    path('timetable/', serve, {'path': 'pycon-balkan-2018-timetable.pdf', 'document_root': PDF_ROOT}, name='timetable'),
    # path('timetable/', timetable_view, name='timetable')
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
