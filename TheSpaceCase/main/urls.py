from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("post/", views.post_page, name="post_page"),
    path("certificate/", views.certificate_page, name="certificate_page"),
    path("company/", views.company_page, name="company_page"),
]