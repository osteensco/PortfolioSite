from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home.html", views.home, name="home"),
    path("projects.html", views.proj_list, name="proj_list"),
    path("<str:name>", views.proj_page, name="proj_page"),
    path("techs.html", views.tech_list, name="tech_list"),
    path("<str:name>", views.tech_page, name="tech_page"),
]