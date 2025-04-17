from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import WorkExperience
# Create your views here.
@csrf_protect
def get_all_workexperience(request):
    workexperiences = WorkExperience.objects.all().order_by("from_date").reverse()
    context = {
        "workexperiences": workexperiences,
    }
    return render(request,template_name="work.html",context=context)
