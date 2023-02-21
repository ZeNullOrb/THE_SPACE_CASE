from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("posts/", views.posts_page, name="posts_page"),
    path("certificates/", views.certificates_page, name="certificates_page"),
]