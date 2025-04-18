"""Application urls"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post-details", views.PostDetail.as_view(), name="post_detail"),
    path("about", views.AboutView.as_view(), name="about"),
]
