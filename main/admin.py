from django.contrib import admin

from .models import (
    Technology, 
    Project, 
    Resume,
    TechType,
    VisualAid,
)
# To register models, add to import statement as well as models list

models = [
    Technology,
    Project,
    Resume,
    TechType,
    VisualAid,
]

for m in models:
    admin.site.register(m)