"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include(('app_aboutMe.urls', 'app_aboutMe'), namespace='app_aboutMe')),
    #path("", include("app_aboutMe.urls")),
    #path("work", include("app_worke.urls", 'work'),namespace="work"),
    path('work', include(('app_worke.urls', 'work'), namespace='app_worke')),
    #path("education", include("app_educatione.urls")),
    #path("education", include(('"app_educatione.urls', 'education'), namespace='"app_educatione')),
    path('education', include(('app_educatione.urls', 'education'), namespace='app_educatione')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path("nl/overmij", include('app_aboutMe.urls',namespace='app_aboutMe')),
    path('nl/vaardigheden', include('app_skills.urls', namespace='app_skills')),
    path('nl/werk', include('app_worke.urls')),
     path('nl/portfolio', include('aportfolio.urls', namespace='portfolio')),
)

urlpatterns += i18n_patterns

#
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)