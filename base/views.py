from django.shortcuts import render
from django.views.generic import TemplateView


# Home view
class HomeView(TemplateView):
    template_name = 'base/index.html'


# About view
class AboutView(TemplateView):
    template_name = 'base/about.html'