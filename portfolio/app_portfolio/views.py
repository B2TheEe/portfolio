from django.shortcuts import render
from .models import PortfolioItem
# Create your views here.

def get_all_portfolio_items(request):
    portfolioitems = PortfolioItem.objects.all()
    context = {
        "portfolioitems": portfolioitems,
    }
    return render(request,template_name="portfolio.html",context=context)

def get_portfolio_item(request, pk):
    portfolio_item = PortfolioItem.objects.get(pk=pk)
    context = {
        "portfolioitem": portfolio_item
    }
    return render(request,template_name="portfolio-item.html", context=context)

