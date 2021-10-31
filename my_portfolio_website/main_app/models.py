from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=100)
    html = models.CharField(max_length=20)
    relevance = models.IntegerField()
    icon = models.ImageField()
    #how to populate all projects tagged with a given technology to it's html file?
    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    html = models.CharField(max_length=20)#html file provides the detailed project description
    relevance = models.IntegerField()
    short_desc = models.CharField(max_length=280)
    repo = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology)
    picture = models.ImageField()
    #technology mix chart like in github? link directly from git repo?
    def __str__(self) -> str:
        return self.name

