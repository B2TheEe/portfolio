from django.shortcuts import render
from .models import WorkExperience
# Create your views here.
def get_all_workexperience(request):
    workexperiences = WorkExperience.objects.all()
    context = {
        "workexperiences": workexperiences,
    }
    return render(request,template_name="work.html",context=context)
