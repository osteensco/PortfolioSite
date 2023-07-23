from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Technology, Project, Resume
from datetime import datetime
from google.oauth2 import service_account
import os
import requests
import json






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





# constants
GCP_KEY = json.loads(os.environ.get('GOOGLE_CLOUD_KEY'))
credentials = service_account.Credentials.from_service_account_file(
    GCP_KEY
)
access_token = credentials.refresh(requests.Request()).headers["Authorization"]
auth_header = {"Authorization": f'''Bearer {access_token}'''}


webhooks = {
    'discord_endpoint': os.environ.get('DISCORD_ENDPOINT'),
    'gcp_endpoint' : os.environ.get('GCP_ENDPOINT')
}

APIs = {
    'pwr_5_teams': os.environ.get('PWR_5_TEAMS_ENDPOINT')
}

year = {'year': datetime.now().year}

resume = {'resume': set_resume()}

defaults =  resume | year






#view functions

#eseentially act as request handlers, URLs will map to one of these functions
def home(response):#provides home page, extended from base. includes all projects and technologies
    projects = Project.objects.order_by('relevance')
    techs = Technology.objects.order_by('relevance')
    display_techs = set_tech_dict(projects)

    #dictionary is used for passing things to html code
    mapping = {
        'title': 'home',
        'projects': projects,
        'techs': techs,
        'display_techs': display_techs
        } | defaults

    return render(response, 'home.html', mapping)


def proj_page(response, name):#queries db for project name and returns appropriate project html file
    project = Project.objects.get(name=name)
    title = project.name
    techs = project.technologies.order_by('relevance')
    visual_aids = {aid.name: aid.img for aid in project.visual_aids.all()}

    mapping = {
        'title': title,
        'project': project,
        'techs': techs
        } | visual_aids | defaults

    return render(response, project.html, mapping)


def tech_page(response, name):#each tech page is extended from basetech.html
    tech = Technology.objects.get(name=name)
    projects = Project.objects.order_by('relevance')
    title = tech.name
    display_techs = set_tech_dict(projects)

    mapping = {
        'title': title,
        'tech': tech,
        'projects': projects,
        'display_techs': display_techs
        } | defaults

    return render(response, 'basetech.html', mapping)

def embed(response, name):
    mapping = {'name': name} | defaults

    return render(response, f'{name}.html', mapping)

def bypass(response):
    return HttpResponse(response)











# APIs

def webhook_API(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        endpoint_name = data.pop('webhook', None)
        if not endpoint_name:
            return JsonResponse({'success': False, 'error': 'webhook variable not found in request body'})
        endpoint_url = webhooks[endpoint_name]
        headers = {
            'Content-type': 'application/json',
        } | auth_header

        try:
            response = requests.post(endpoint_url, data=json.dumps(data), headers=headers)
            response.raise_for_status()

            return JsonResponse({'success': True})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'success': False, 'error': str(e)})


def API_call(request):
    if request.method == 'GET':
        params =  request.GET.dict()
        print(params)
        print('\n\n')
        endpoint_name = params.pop('API', None)
        if not endpoint_name:
            return JsonResponse({'success': False, 'error': 'API variable not found in request body'})
        endpoint_url = APIs[endpoint_name]
        
        try:
            response = requests.get(endpoint_url, params=params, headers=auth_header)
            response.raise_for_status()

            data = {'response': response.json()}
            return JsonResponse(data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)})



