"""Application views"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page"""
    template_name = "index.html"


class AboutView(TemplateView):
    """About page"""
    template_name = "about.html"
