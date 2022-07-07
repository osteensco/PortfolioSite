from django.contrib import admin

from .models import (
    Technology, 
    Project, 
    Resume,
    TechType,

)
# To register models, add to import statement as well as models list

models = [
    Technology,
    Project,
    Resume,
    TechType,
    
]

for m in models:
    admin.site.register(m)