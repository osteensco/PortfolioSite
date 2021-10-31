from django.shortcuts import render
from .models import Technology, Project


def home(response):
    title = '''Scott Osteen's Portfolio'''
    return render(response, 'home.html', {'title': title})#dictionary is used for passing things to html code


def proj_list(response):
    projects = Project.objects.order_by('relevance')
    title = "All Projects"
    return render(response, 'projects.html', {'title': title, 'projects': projects})


def tech_list(response):
    techs = Technology.objects.order_by('relevance')
    title = "Technologies"
    return render(response, 'techs.html', {'title': title, 'techs': techs})


def proj_page(response, id):
    project = Project.objects.get(id=id)
    title = project.name
    return render(response, project.html, {'title': title, 'project': project})


def tech_page(response, id):
    tech = Technology.objects.get(id=id)
    title = tech.name
    return render(response, tech.html, {'title': title, 'tech': tech})