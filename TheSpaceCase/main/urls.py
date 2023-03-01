from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("profile/", views.profile_page, name="profile_page"),
    path("apply/<apply_id>", views.apply_content, name="apply_content"),


    path("post/", views.post_page, name="post_page"),
    path("add/post/", views.add_post, name="add_post"),
    path("view/post/<post_id>/", views.view_post, name="view_post"),
    path("update/post/<post_id>/", views.update_post, name="update_post"),
    path("delete/post/<post_id>/", views.delete_post, name="delete_post"),

    path("certificate/", views.certificate_page, name="certificate_page"),
    path("add/certificate/", views.add_certificate, name="add_certificate"),
    path("view/certificate/<certificate_id>/", views.view_certificate, name="view_certificate"),
    path("update/certificate/<certificate_id>/", views.update_certificate, name="update_certificate"),
    path("delete/certificate/<certificate_id>/", views.delete_certificate, name="delete_certificate"),

    path("company/", views.company_page, name="company_page"),
    path("add/company/", views.add_company, name="add_company"),
    path("view/company/<company_id>/", views.view_company, name="view_company"),
    path("update/company/<company_id>/", views.update_company, name="update_company"),
    path("delete/company/<company_id>/", views.delete_company, name="delete_company"),
]