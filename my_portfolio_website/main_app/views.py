from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return render(response, "home.html", {})#dictionary is used for passing things to html code

