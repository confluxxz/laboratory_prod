from django.contrib import admin
from goods.models import Categories, Items

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_display = ['name']


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'category__name']
    list_display = ['name', 'quantity', 'existence']
    # list_editable = ['existence']
    list_filter = ['name', 'quantity', 'existence']
    fields = [
        ("name", "category"),
        "slug",
        "description",
        ("image", "additional_image"),
        ("quantity", "existence"),
        ("units", "working_type"),


    ]