from django.urls import path
from . import views
from django.views.generic import TemplateView




#request will hit every list item until first argument matches the GET request

urlpatterns = [
    path("favicon.ico", views.bypass),
    path("webhooks/", views.webhook_API, name="webhooks"),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("tech/<str:name>/", views.tech_page, name="tech_page"),
    path("projects/<str:name>/", views.proj_page, name="proj_page"),
    # path("projects/visuals/embeds/<str:name>/", views.embed, name="embed"),
    path("projects/visuals/embeds/pong/", TemplateView.as_view(template_name="pong_embed.html"), name='pong_embed')
]

