from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home.html", views.home, name="home"),
    path("<int:id>", views.tech_page, name="tech_page"),
    path("<str:name>", views.proj_page, name="proj_page"),
    
]