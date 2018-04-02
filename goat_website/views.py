from django.shortcuts import render
from django.views.generic import TemplateView

class ByePage(TemplateView):
    template_name = 'bye.html'

class WelcomePage(TemplateView):
    template_name = 'welcome.html'
