from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "test": 'test',
    }
    return render(request, "portfolio.html",context=data)