"""whoa URL Configuration

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
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from xadmin.plugins import xversion
import xadmin
import demo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'demo/', include('demo.urls')),
    url(r'oa/', include('oa.urls')),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
