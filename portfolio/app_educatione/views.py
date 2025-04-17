from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import EducationExperience

# Create your views here.
@csrf_protect
def get_all_educationexperience(request):
    educationxperiences = EducationExperience.objects.all().order_by("from_date").reverse()
    context = {
        "educationexperiences": educationxperiences,
    }
    return render(request,template_name="education.html",context=context)