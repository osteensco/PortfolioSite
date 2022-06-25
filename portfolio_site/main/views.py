from django.shortcuts import render
from django.http import HttpResponse
from .models import Technology, Project



def home(response):
    return HttpResponse("<h1>Home Page</h1>")