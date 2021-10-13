from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import PortfolioProject


def home(request):
    return render(request, 'html/home.html')


def about_me(request):
    return render(request, 'html/about-me.html')


def portfolio(request):
    portfolio_items = PortfolioProject.objects.all()
    context = {'portfolio': portfolio_items}
    return render(request, 'html/portfolio.html', context)


def contact(request):
    return render(request, 'html/contact.html')


def portfolioProjectView(request, id):
    project = PortfolioProject.objects.get(id=id)
    context = {'project' : project}

    return render(request, 'html/project.html', context)
