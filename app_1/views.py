from django.shortcuts import render
from django.views.generic import TemplateView   # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class secondHomePageView(TemplateView):
    template_name = 'about.html'

class newsPageView(TemplateView):
    template_name = 'news.html'

class imagesPageView(TemplateView):
    template_name = 'images.html'

class Admin(TemplateView):
    template_name = 'admin.html'