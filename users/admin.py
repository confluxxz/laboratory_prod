from django.contrib import admin
from users.models import User
from experiments.admin import ExperimentTabularAdmin
from works.admin import WorkTabularAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'username', 'email']
    list_display = ['first_name', 'last_name', 'username', 'email']

    inlines = [ExperimentTabularAdmin, WorkTabularAdmin,]