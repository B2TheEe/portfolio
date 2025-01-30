from django.db.models.functions import Coalesce
from django.shortcuts import render
from .models import WorkExperience
# Create your views here.
def get_all_workexperience(request):
    workexperiences = WorkExperience.objects.all().order_by("from_date")
    context = {
        "workexperiences": workexperiences,
    }
    return render(request,template_name="work.html",context=context)
