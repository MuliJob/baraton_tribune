"""Application views"""
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(APIView):
    """API view for home"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        """Get method"""

        return Response({}, template_name=self.template_name)


class CategoryView(APIView):
    """API view for categories"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category.html'

    def get(self, request, *args, **kwargs):
        """Get method"""

        return Response({}, template_name=self.template_name)


class PostDetail(APIView):
    """API view for post details"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'post-details.html'

    def get(self, request, *args, **kwargs):
        """Get method"""

        return Response({}, template_name=self.template_name)


class AuthorDetail(APIView):
    """API view for author details"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'author-profile.html'

    def get(self, request, *args, **kwargs):
        """Get method"""

        return Response({}, template_name=self.template_name)


class AboutView(APIView):
    """API view for about"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        """Get method"""

        return Response({}, template_name=self.template_name)


class ContactView(APIView):
    """API view for contact"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        """Get method"""

        return Response({}, template_name=self.template_name)
