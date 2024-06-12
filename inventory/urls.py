from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.reagents import ReagentsModelViewSet, WorkReagentsModelViewSet, UnitsTypeView
from .views.works import WorksModelViewSet, WorkStudentModelViewSet, WorkTeacherModelViewSet
from .views.equipment import EquipmentModelViewSet
from .views.result import ResultModelViewSet
from .views.extra_fields import ExtraFieldsModelViewSet
from .views.value_extra_fields import ValueModelViewSet
from .views.equipment_drymethod import EquipmentDryMethodModelViewSet

inventory_router = SimpleRouter()
inventory_router.register(prefix='reagents', viewset=ReagentsModelViewSet, basename='reagents')
inventory_router.register(prefix='works', viewset=WorksModelViewSet, basename='works')


work_reagents_router = SimpleRouter()
work_reagents_router.register(prefix='reagents', viewset=WorkReagentsModelViewSet, basename='work|reagents')

equipment_router = SimpleRouter()
equipment_router.register(prefix='equipments', viewset=EquipmentModelViewSet, basename='equipments')

result_router = SimpleRouter()
result_router.register(prefix='result', viewset=ResultModelViewSet, basename='work|result')

extra_field_router = SimpleRouter()
extra_field_router.register(prefix='extra_field', viewset=ExtraFieldsModelViewSet, basename='extra_field')

value_extra_field_router = SimpleRouter()
value_extra_field_router.register(prefix='value', viewset=ValueModelViewSet, basename='value')\

dry_method_router = SimpleRouter()
dry_method_router.register(prefix='dry_method', viewset=EquipmentDryMethodModelViewSet, basename='dry_method')


student_router = SimpleRouter()
student_router.register(prefix='work', viewset=WorkStudentModelViewSet, basename='student|works')

teacher_router = SimpleRouter()
teacher_router.register(prefix='work', viewset=WorkTeacherModelViewSet, basename='teacher|works')

urlpatterns = [
    path('', include(inventory_router.urls)),
    path('works/<int:work_id>/', include(work_reagents_router.urls)),
    path('units/type/', view=UnitsTypeView.as_view(), name='units|type'),
    path('', include(equipment_router.urls)),
    path('', include(result_router.urls)),
    path('', include(extra_field_router.urls)),
    path('', include(value_extra_field_router.urls)),
    path('', include(dry_method_router.urls)),
    path('student/', include(student_router.urls)),
    path('teacher/', include(teacher_router.urls)),

]
