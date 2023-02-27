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

# -----------------------------------------------------------------------------------------------------------------

def post_page(request : HttpRequest):
    
    view_post = Post.objects.all()

    context = {"view_post" : view_post}
    return render(request, "main/post.html", context)

def add_post(request : HttpRequest):

    if not request.user.has_perm("main.add_post"):
        return redirect("main/no_permission.html")

    if request.method == "POST":
        company = Company.objects.get(id=request.POST["company"])
        certificates = Certificate.objects.get(id=request.POST["certificate"])
        #to add a new entry
        new_post = Post(title= request.POST["title"], content = request.POST["content"], company=company)
        new_post.save()
        new_post.certificate.add(certificates)
        new_post.save()
        return redirect("main:post_page")
    
    companies = Company.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'add_update/add_post.html', {'companies':companies,'certificates':certificates})

# -----------------------------------------------------------------------------------------------------------------

def certificate_page(request : HttpRequest):
    view_certificate = Certificate.objects.all()

    context = {"view_certificate" : view_certificate}
    return render(request, "main/certificate.html", context)

def view_certificate(request : HttpRequest,certificate_id):
    view_certificate = Certificate.objects.get(id=certificate_id)

    context = {"view_certificate" : view_certificate}
    return render(request, "main/view_certificate.html", context)

# -----------------------------------------------------------------------------------------------------------------

def company_page(request : HttpRequest):
    view_company = Company.objects.all()

    context = {"view_company" : view_company}
    return render(request, "main/company.html", context)

