from django.contrib.admin import site, ModelAdmin
from .models.request import Request


class RequestModelAdmin(ModelAdmin):
    pass


site.register(Request, RequestModelAdmin)