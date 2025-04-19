"""Application views"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page"""
    template_name = "index.html"

class CategoryView(TemplateView):
    """Category Page"""
    template_name = "category.html"

class PostDetail(TemplateView):
    """Post Detail Page"""
    template_name = "post-details.html"

class AboutView(TemplateView):
    """About page"""
    template_name = "about.html"
