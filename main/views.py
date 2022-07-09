from django.shortcuts import render
from django.http import HttpResponse
from .models import Technology, Project, Resume

#more akin to request handlers, these functions provide a response from a request. depends upon hit in urls list.

def home(response):#provides home page, extended from base. includes all projects and technologies
    title = '''Scott Osteen's Portfolio'''
    projects = Project.objects.order_by('relevance')
    techs = Technology.objects.order_by('relevance')
    try:
        resume = Resume.objects.get(current=True)
    except Resume.DoesNotExist:
        resume = None
    
    displaytechs = {}
    for project in projects:#manifest list of technologies used for each project
        l = [tech for tech in project.technologies.order_by('relevance')]
        d = {f'''{project.name}''': l}
        displaytechs = displaytechs | d

    mapping = {
        'title': title,
        'projects': projects,
        'techs': techs,
        'resume': resume,
        'displaytechs': displaytechs
        }#dictionary is used for passing things to html code

    return render(response, 'home.html', mapping)


def proj_page(response, name):#queries db for project name and returns appropriate project html file
    project = Project.objects.get(name=name)
    title = project.name
    techs = project.technologies.order_by('relevance')

    try:
        resume = Resume.objects.get(current=True)
    except Resume.DoesNotExist:
        resume = None

    mapping = {
        'title': title,
        'project': project,
        'techs': techs,
        'resume': resume
        }

    return render(response, project.html, mapping)


def tech_page(response, name):#each tech page is extended from basetech.html
    tech = Technology.objects.get(name=name)
    projects = Project.objects.order_by('relevance')
    title = tech.name

    try:
        resume = Resume.objects.get(current=True)
    except Resume.DoesNotExist:
        resume = None

    mapping = {
        'title': title,
        'tech': tech,
        'projects': projects,
        'resume': resume
        }

    return render(response, 'basetech.html', mapping)

def bypass(response):
    return HttpResponse(response)