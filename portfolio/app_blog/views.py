from django.shortcuts import render
from .models import BlogArticle

# Create your views here.
def get_all_blogs(request):
    blogs = BlogArticle.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request,"blogarticles.html",context=context)
