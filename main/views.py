from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import PortfolioProject


def home(request):
    return render(request, 'html/home.html')


def about_me(request):
    return render(request, 'html/about-me.html')

def portfolio(request):
    return render(request, 'html/portfolio.html')


def contact(request):
    return render(request, 'html/contact.html')
