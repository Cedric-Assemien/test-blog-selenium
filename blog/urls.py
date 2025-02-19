from django.urls import path
from blog import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("blog/<int:pk>", views.blog_details, name="blog-details"),
]
