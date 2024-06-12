from django.contrib import admin
from works.models import Work, WorkItem


class WorkItemTabularAdmin(admin.TabularInline):
    model = WorkItem
    fields = "item", "name", "quantity"
    search_fields = (
        "item",
        "name"
    )
    extra = 0


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "name", "description",
        "requires_files", "additional_files",
        "status_experiment",
        "is_done", "results",
        "created_timestamp"
    )
    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "status_experiment",
        "is_done"
    )
    inlines = (WorkItemTabularAdmin,)

@admin.register(WorkItem)
class WorkItemAdmin(admin.ModelAdmin):
    list_display = "work", "item", "name", "quantity"
    search_fields = (
        "work",
        "item",
        "name",
    )


class WorkTabularAdmin(admin.TabularInline):
    model = Work
    fields = (
        "requires_files", "additional_files",
        "is_done", "status_experiment",
        "created_timestamp"

    )
    search_fields = (
        "requires_files",
        "is_done",
        "created_timestamp"
    )
    readonly_fields = ("created_timestamp",)
    extra = 0