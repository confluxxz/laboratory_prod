from django.contrib.admin import site, ModelAdmin
from .models.dishes import Dishes


class DishesModelAdmin(ModelAdmin):
    search_fields = ['name', 'place']


site.register(Dishes, DishesModelAdmin)

