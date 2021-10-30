from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField()
    #does each need its own "home" page?


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=280)
    technologies = models.ManyToManyField(Technology)
    picture = models.ImageField()
    #technology mix chart like in github? link directly from git repo?
    #each definitely needs its own "details" page