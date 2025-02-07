from django.shortcuts import render
from .models import PortfolioItem
# Create your views here.
def get_all_portfolio_items(request):
    portfolioitems = PortfolioItem.objects.all()
    context = {
        "portfolioitems": portfolioitems,
    }
    return render(request,template_name="education.html",context=context)