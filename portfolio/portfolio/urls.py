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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('aboutMe.urls', 'aboutMe'), namespace='aboutMe')),
    #path("", include("aboutMe.urls")),
    #path("work", include("worke.urls", 'work'),namespace="work"),
    path('work', include(('worke.urls', 'work'), namespace='work')),
    #path("education", include("educatione.urls")),
    path("education", include(('"education.urls', 'education'), namespace='"education')),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

i18n_patterns = [
    #path("nl/overmij", include('aboutMe.urls',namespace='aboutMe')),
    #path('nl/vaardigheden', include('skills.urls', namespace='skills')),
    path('nl/werk', include('worke.urls')),
   # path('nl/portfolio', include('aportfolio.urls', namespace='portfolio')),
    path('nl/admin', admin.site.urls),
]
urlpatterns += i18n_patterns
