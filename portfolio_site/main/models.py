from django.db import models



class Technology(models.Model):
    name = models.CharField(max_length=100)
    relevance = models.IntegerField()
    icon = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    html = models.CharField(max_length=50)#text here will populate in html template, provides the detailed project description
    relevance = models.IntegerField()
    short_desc = models.CharField(max_length=280)
    repo = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology)
    icon = models.ImageField()
    #technology mix chart like in github? link directly from git repo?

    def __str__(self) -> str:
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=100, default='ScottOsteenResume')
    current = models.BooleanField(default=True)
    pdf = models.FileField(upload_to='static/')

    def __str__(self) -> str:
        return self.name

        