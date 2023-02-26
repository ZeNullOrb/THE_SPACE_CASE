from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Company,Certificate,Post,Contact

# Create your views here.


def main_page(request : HttpRequest):

    companies = Company.objects.all()
    posts = Contact.objects.all()
    users = User.objects.all()
    certificates = Certificate.objects.all()
    
    return render(request, 'main/index.html', {'companies':companies,'posts':posts,'users':users,'certificates':certificates})

def contact_page(request : HttpRequest):
    view_contact = Contact.objects.all()

    context = {"view_contact" : view_contact}
    return render(request, "main/contact.html", context)

def post_page(request : HttpRequest):
    
    view_post = Post.objects.all()

    context = {"view_post" : view_post}
    return render(request, "main/post.html", context)

def certificate_page(request : HttpRequest):
    view_certificate = Certificate.objects.all()

    context = {"view_certificate" : view_certificate}
    return render(request, "main/certificate.html", context)

def company_page(request : HttpRequest):
    view_company = Company.objects.all()

    context = {"view_company" : view_company}
    return render(request, "main/company.html", context)
