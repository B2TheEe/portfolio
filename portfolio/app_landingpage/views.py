import os

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.http import FileResponse
from .models import LandingPage

# Create your views here.

def index(request):
    try:
        lp = LandingPage.objects.get(pk=1)
        return render(request, "index.html", {"landingpage": lp,  })
    except LandingPage.DoesNotExist:
        raise Http404("No Landingpage matches the given query.")


def download_cv(reauest):
        return FileResponse(open('media/documents/CV_BenteSchopman_EN_v0125_GSkfl1A.pdf', 'rb'), as_attachment=True, content_type='application/pdf')