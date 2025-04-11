import os

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from .models import LandingPage

# Create your views here.

def index(request):
    try:
        lp = LandingPage.objects.get(pk=1)
        return render(request, "index.html", {"landingpage": lp,  })
    except LandingPage.DoesNotExist:
        raise Http404("No Landingpage matches the given query.")


def download_cv(request):
    lang = settings.LANGUAGE_CODE

    if lang == 'en-us':
      return FileResponse(open('media/documents/CV_BenteSchopman_EN_v0125_8ZoYu50.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
    else:
      return FileResponse(open('media/documents/CV_BenteSchopman_NL_v0125_5RzvHIB.pdf', 'rb'), as_attachment=True,
                            content_type='application/pdf')

