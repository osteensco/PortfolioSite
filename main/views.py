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
        l = [tech.name for tech in project.technologies.all()]
        l = str(l)[1:-1]
        d = {f'''{project.name}''': f'''{l.replace("'","")}'''}
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

    return render(response, project.html, {'title': title, 'project': project})


def tech_page(response, name):#each tech page is extended from basetech.html
    tech = Technology.objects.get(name=name)
    projects = Project.objects.order_by('relevance')
    title = tech.name

    return render(response, 'basetech.html', {'title': title, 'tech': tech, 'projects': projects})

def bypass(response):
    return HttpResponse(response)