from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#request will hit every list item until first argument matches the GET request

urlpatterns = [
    path("favicon.ico", views.bypass),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("tech/<str:name>/", views.tech_page, name="tech_page"),
    path("projects/<str:name>/", views.proj_page, name="proj_page"),
]

