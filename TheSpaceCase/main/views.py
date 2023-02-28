from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Company,Certificate,Post,Contact
from django.db import IntegrityError

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

def profile_page(request : HttpRequest): 
    
    user : User = request.user
    update_msg = None
    def username_auth(username_check):
        user : User = request.user
        if username_check in request.FILES:
            if User.objects.filter(username=request.POST['username']).exists():
                update_msg = "User already exist"
                return render(request, "main/profile.html", {"msg" : update_msg})
            else:
                user.username = request.POST['username']
                user.save()
    if request.method == "POST":
        username_check = request.POST['username']
        username_auth(username_check)
        user.first_name = request.POST["first_name"]   
        user.last_name = request.POST["last_name"]     
        user.email = request.POST["email"]
        user.save()
        update_msg = "Updated successfully!"

        return render(request, "main/profile.html", {"msg" : update_msg})

        
    context = {"user" : user, "msg" : update_msg}
    return render(request, "main/profile.html", context)




# ---------------------------------------------------POST-----------------------------------------------------------

def post_page(request : HttpRequest):
    
    view_post = Post.objects.all()

    context = {"view_post" : view_post}
    return render(request, "main/post.html", context)

def add_post(request : HttpRequest):

    if not request.user.has_perm("main.add_post"):
        return redirect("accounts:no_permission")

    if request.method == "POST":
        company = Company.objects.get(id=request.POST["company"])
        certificates = Certificate.objects.get(id=request.POST["certificate"])
        #to add a new post
        new_post = Post(title= request.POST["title"], content = request.POST["content"], company=company)
        new_post.save()
        new_post.certificate.add(certificates)
        new_post.save()
        return redirect("main:post_page")
    
    companies = Company.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'main/add_post.html', {'companies':companies,'certificates':certificates})

def update_post(request : HttpRequest, post_id):

    if not request.user.has_perm("main.update_post"):
        return redirect("accounts:no_permission")

    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        company = Company.objects.get(id=request.POST["company"])
        certificates = Certificate.objects.get(id=request.POST["certificate"])
        #to update a post
        post.title = request.POST["title"] 
        post.content = request.POST["content"]
        post.company=company
        post.save()
        post.certificate.add(certificates)
        post.save()
        return redirect("main:post_page")
    
    companies = Company.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'main/update_post.html', {'companies':companies,'certificates':certificates,"post":post})

def delete_post(request : HttpRequest, post_id):

    if not request.user.has_perm("main.delete_post"):
        return redirect("accounts:no_permission")
    
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("main:post_page")

def view_post(request : HttpRequest,post_id):
    view_post = Post.objects.get(id=post_id)

    context = {"view_post" : view_post}
    return render(request, "main/view_post.html", context)

# ---------------------------------------------------CERTIFICATE-----------------------------------------------------------

def certificate_page(request : HttpRequest):
    view_certificate = Certificate.objects.all()

    context = {"view_certificate" : view_certificate}
    return render(request, "main/certificate.html", context)

def add_certificate(request : HttpRequest):

    if not request.user.has_perm("main.add_certificate"):
        return redirect("accounts:no_permission")

    if request.method == "POST":

        #to add a new certificate
        new_certificate = Certificate(name= request.POST["name"],
                                      issuing_organization= request.POST["issuing_organization"],
                                      certificate_id= request.POST["certificate_id"],
                                      certificate_url= request.POST["certificate_url"],)
        new_certificate.save()
        return redirect("main:certificate_page")
    
    return render(request, 'main/add_certificate.html')

def update_certificate(request : HttpRequest, certificate_id):

    certificate = Certificate.objects.get(id=certificate_id)

    if not request.user.has_perm("main.update_certificate"):
        return redirect("accounts:no_permission")

    if request.method == "POST":

        #to update a certificate
        certificate.name= request.POST["name"]
        certificate.issuing_organization= request.POST["issuing_organization"]
        certificate.certificate_id= request.POST["certificate_id"]
        certificate.certificate_url= request.POST["certificate_url"]
        certificate.save()
        return redirect("main:certificate_page")
    
    return render(request, 'main/update_certificate.html', {"certificate": certificate})

def delete_certificate(request : HttpRequest, certificate_id):

    if not request.user.has_perm("main.delete_certificate"):
        return redirect("accounts:no_permission")
    
    certificate = Certificate.objects.get(id=certificate_id)
    certificate.delete()
    return redirect("main:certificate_page")

def view_certificate(request : HttpRequest,certificate_id):
    view_certificate = Certificate.objects.get(id=certificate_id)

    context = {"view_certificate" : view_certificate}
    return render(request, "main/view_certificate.html", context)

# ---------------------------------------------------COMPANY-----------------------------------------------------------

def company_page(request : HttpRequest):
    view_company = Company.objects.all()

    context = {"view_company" : view_company}
    return render(request, "main/company.html", context)

def view_company(request : HttpRequest,company_id):
    view_company = Company.objects.get(id=company_id)

    context = {"view_company" : view_company}
    return render(request, "main/view_company.html", context)