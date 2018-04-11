"""pyconbalkan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from pyconbalkan.core import views
from pyconbalkan.settings import BASE_DIR, PDF_PATH

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^coc$', serve, {'path': 'coc_pyconbalkan.pdf', 'document_root': os.path.join(BASE_DIR, PDF_PATH)}),
    url(r'^admin/', admin.site.urls),
]
