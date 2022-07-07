from django.db import models



#######ADD MODELS TO ADMIN.PY AFTER MIGRATION###############

class TechType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TechType, null=True, on_delete=models.SET_NULL)
    relevance = models.IntegerField()
    icon = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    html = models.CharField(max_length=50)#maps to html file, extends from baseproj template
    relevance = models.IntegerField()
    short_desc = models.CharField(max_length=280)
    repo = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology)
    icon = models.ImageField(upload_to="images/")
    #technology mix chart?

    def __str__(self) -> str:
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=100, default='ScottOsteenResume')
    current = models.BooleanField(default=True)
    pdf = models.FileField(upload_to="resume/")

    def __str__(self) -> str:
        return self.name


#######ADD MODELS TO ADMIN.PY AFTER MIGRATION###############
