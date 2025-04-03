import os

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import LandingPage

# Create your views here.

def index(request):
    try:
        lp = LandingPage.objects.get(pk=1)
        return render(request, "index.html", {"landingpage": lp,  })
    except LandingPage.DoesNotExist:
        raise Http404("No Landingpage matches the given query.")

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404