"""Application urls"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("category", views.CategoryView.as_view(), name="category"),
    path("post-details", views.PostDetail.as_view(), name="post_detail"),
    path("author-profile", views.AuthorDetail.as_view(), name="author"),
    path("about", views.AboutView.as_view(), name="about"),
]
