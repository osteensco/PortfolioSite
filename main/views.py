from django.shortcuts import render
from django.http import HttpResponse
from .models import Technology, Project, Resume
import os



#helper functions
def set_tech_dict(projects):
    dt = {}
    for project in projects:#manifest list of technologies used for each project
        l = [tech for tech in project.technologies.order_by('relevance')]
        d = {f'''{project.name}''': l}
        dt = dt | d

    return dt

def set_resume():
    try:
        r = Resume.objects.get(current=True)
    except Resume.DoesNotExist:
        r = None
    
    return r


webhooks = {
    'discord_endpoint': os.environ.get('DISCORD_ENDPOINT')

}

#view functions
#more akin to request handlers, these functions provide a response from a request. depends upon hit in urls list.
def home(response):#provides home page, extended from base. includes all projects and technologies
    title = '''Scott Osteen's Portfolio'''
    projects = Project.objects.order_by('relevance')
    techs = Technology.objects.order_by('relevance')
    display_techs = set_tech_dict(projects)
    resume = set_resume()

    #dictionary is used for passing things to html code
    mapping = {
        'title': title,
        'projects': projects,
        'techs': techs,
        'resume': resume,
        'display_techs': display_techs
        } | webhooks

    return render(response, 'home.html', mapping)


def proj_page(response, name):#queries db for project name and returns appropriate project html file
    project = Project.objects.get(name=name)
    title = project.name
    techs = project.technologies.order_by('relevance')
    visual_aids = {aid.name: aid.img for aid in project.visual_aids.all()}
    resume = set_resume()

    mapping = {
        'title': title,
        'project': project,
        'techs': techs,
        'resume': resume
        } | visual_aids | webhooks

    return render(response, project.html, mapping)


def tech_page(response, name):#each tech page is extended from basetech.html
    tech = Technology.objects.get(name=name)
    projects = Project.objects.order_by('relevance')
    title = tech.name
    display_techs = set_tech_dict(projects)
    resume = set_resume()

    mapping = {
        'title': title,
        'tech': tech,
        'projects': projects,
        'resume': resume,
        'display_techs': display_techs
        } | webhooks

    return render(response, 'basetech.html', mapping)

def embed(response, name):
    mapping = {'name': name} | webhooks

    return render(response, f'{name}.html', mapping)





def bypass(response):
    return HttpResponse(response)


