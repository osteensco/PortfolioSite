from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#request will hit every list item until first argument matches the GET request

urlpatterns = [
    path("favicon.ico", views.bypass),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("<int:id>", views.tech_page, name="tech_page"),
    path("<str:name>", views.proj_page, name="proj_page"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#https://stackoverflow.com/questions/56886558/page-is-not-found-while-downloading-the-file-in-django
# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)