from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    title = '''Scott Osteen's Portfolio'''
    return render(response, "home.html", {'title': title})#dictionary is used for passing things to html code

