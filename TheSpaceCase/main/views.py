from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Company,Certificate,Post,Contact,ApplyContent
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
        
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists():
            # update_msg = "User already exist"
            exit
        else:
            user.username = request.POST['username']
            # update_msg = "Updated successfully!"
        user.first_name = request.POST["first_name"]   
        user.last_name = request.POST["last_name"]     
        user.email = request.POST["email"]
        user.save()

        return render(request, "main/profile.html", {"msg" : update_msg})

        
    context = {"user" : user, "msg" : update_msg}
    return render(request, "main/profile.html", context)


def apply_content(request : HttpRequest,apply_id):
    
    user : User = request.user
    post = Post.objects.get(id=apply_id)

    apply = ApplyContent(
        company = post.company,
        title = post.title,
        name = user.first_name,
        email = user.email
    )
    apply.save()

    return redirect("main:post_page")



# ---------------------------------------------------POST-----------------------------------------------------------

def post_page(request : HttpRequest):
    
    view_post = Post.objects.all()

    context = {"view_post" : view_post}
    return render(request, "main/post.html", context)

def add_post(request : HttpRequest):

    if not request.user.has_perm("main.add_post"):
        return redirect("accounts:no_permission")
    
    if request.method == "POST":
        company = Company.objects.get(name=request.POST["company"])
        #to add a new post
        new_post = Post(title= request.POST["title"], content = request.POST["content"], company=company,image = request.FILES["image"])
        new_post.save()
        certificateList = request.POST.getlist('certificate_list')
        for certificate in certificateList:
            certificateItem = Certificate.objects.get(id=certificate)
            new_post.certificate.add(certificateItem)
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
        
        #to update a post
        post.title = request.POST["title"] 
        post.content = request.POST["content"]
        post.company=company
        post.save()
        certificateList = request.POST.getlist('certificate_list')
        for certificate in certificateList:
            certificateItem = Certificate.objects.get(id=certificate)
            post.certificate.add(certificateItem)
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

def add_company(request : HttpRequest):

    if not request.user.has_perm("main.add_company"):
        return redirect("accounts:no_permission")

    if request.method == "POST":

        #to add a new company
        new_company = Company(name= request.POST["name"],
                              image = request.FILES["image"],
                              email= request.POST["email"],
                              address= request.POST["address"],
                              phone= request.POST["phone"],
                              website= request.POST["website"],
                              description= request.POST["description"],
                            )
        new_company.save()
        return redirect("main:company_page")
    
    return render(request, 'main/add_company.html')

def update_company(request : HttpRequest, company_id):

    company = Company.objects.get(id=company_id)

    if not request.user.has_perm("main.update_company"):
        return redirect("accounts:no_permission")

    if request.method == "POST":

        #to update a company
        company.name= request.POST["name"]
        if "image" in request.FILES:
            company.image = request.FILES["image"]
        company.email= request.POST["email"]
        company.address= request.POST["address"]
        company.phone= request.POST["phone"]
        company.website= request.POST["website"]
        company.description= request.POST["description"]
        company.save()
        return redirect("main:company_page")
    
    return render(request, 'main/update_company.html', {"company": company})

def delete_company(request : HttpRequest, company_id):

    if not request.user.has_perm("main.delete_company"):
        return redirect("accounts:no_permission")
    
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect("main:company_page")

def view_company(request : HttpRequest,company_id):
    view_company = Company.objects.get(id=company_id)

    context = {"view_company" : view_company}
    return render(request, "main/view_company.html", context)