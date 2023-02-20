from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main_page(request : HttpRequest):
    
    return render(request, 'main/index.html')

