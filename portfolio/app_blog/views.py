from django.shortcuts import render
from .models import BlogArticle

# Create your views here.
def get_all_blogs(request):
    blogs = BlogArticle.objects.filter(status=1)
    context = {
        "blogs": blogs,
    }
    return render(request,"blogarticles.html",context=context)

def get_blog(request, pk):
    blogarticle = BlogArticle.objects.get(pk=pk)
    context = {
        "blogarticle": blogarticle,
    }
    return render(request,template_name="blogarticle.html", context=context)

