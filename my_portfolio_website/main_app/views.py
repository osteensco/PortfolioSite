from django.shortcuts import render
from .models import Technology, Project


def home(response):
    title = '''Scott Osteen's Portfolio'''
    projects = Project.objects.order_by('relevance')
    techs = Technology.objects.order_by('relevance')

    return render(response, 'home.html', {'title': title, 'projects': projects, 'techs': techs})#dictionary is used for passing things to html code


def proj_page(response, name):
    project = Project.objects.get(name=name)
    title = project.name

    return render(response, project.html, {'title': title, 'project': project})


def tech_page(response, id):
    tech = Technology.objects.get(id=id)
    projects = Project.objects.order_by('relevance')
    title = tech.name

    return render(response, 'basetech.html', {'title': title, 'tech': tech, 'projects': projects})