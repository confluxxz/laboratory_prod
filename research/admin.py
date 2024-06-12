from django.contrib.admin import site, ModelAdmin
from .models.research import Research

class ResearchModelAdmin(ModelAdmin):
    pass

class WorkRequestModelAdmin(ModelAdmin):
    pass

site.register(Research, ResearchModelAdmin)
