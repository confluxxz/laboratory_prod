from django.contrib.admin import site, ModelAdmin

from .models import ExtraFields, Reagents, WorkReagents, Work, Result, Value, DryMethod, Equipment


class ReagentsModelAdmin(ModelAdmin):
    search_fields = ['name', 'place']


class WorkReagentsModelAdmin(ModelAdmin):
    pass


class WorkModelAdmin(ModelAdmin):
    pass


class ResultModelAdmin(ModelAdmin):
    pass


class ExtraFieldModelAdmin(ModelAdmin):
    pass


class ValueModelAdmin(ModelAdmin):
    pass


class DryMethodModelAdmin(ModelAdmin):
    pass

class EquipmentModelAdmin(ModelAdmin):
    search_fields = ['name', 'place']


site.register(Reagents, ReagentsModelAdmin)
site.register(WorkReagents, WorkReagentsModelAdmin)
site.register(Work, WorkModelAdmin)
site.register(Result, ResultModelAdmin)
site.register(ExtraFields, ExtraFieldModelAdmin)
site.register(Value, ValueModelAdmin)
site.register(DryMethod, DryMethodModelAdmin)
site.register(Equipment, EquipmentModelAdmin)


