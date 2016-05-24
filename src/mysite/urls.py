"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from vulnerability import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^vulnerability/NVDlist/$', views.vulnerabilityNVD),
    url(r'^vulnerability/searchAdvanced/$', views.search_advanced),
    url(r'^detail/$', views.detailVul),
    url(r'^search/\??$', views.searchVul),
    url(r'^NVDlist/$', views.vulnerabilityNVD),
    url(r'^vulnerability/Patchlist/$', views.vulnerabilityPatch),
    url(r'^vulnerability/Reuselist/$', views.vulnerabilityReuse),
    url(r'^vulnerability/aboutFeature/$', views.featureShow),
    url(r'^diffInfo/$', views.diffInfoShow),
    url(r'^download/$', views.download),
    
]
