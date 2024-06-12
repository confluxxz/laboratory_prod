#
# # урлы
#
#
# from django.db.models import Model, ForeignKey, TextField, CharField, BooleanField
# from django.db.models.deletion import CASCADE
# from clients.models.client import ClientSystem
# from research.models import Research
#
#
# class Work(Model):
#     name = CharField(max_length=100, verbose_name='Наименование')
#     description = TextField(null=True, blank=True, verbose_name='Описание')
#     student = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='student', verbose_name='Студент')
#     accept_person = ForeignKey(to=ClientSystem, on_delete=CASCADE, default=None, blank=True, null=True,
#                                related_name='accept_persons', verbose_name='Согласующий')
#     research = ForeignKey(to=Research, on_delete=CASCADE, related_name='works', verbose_name='Исследование',
#                           default=None)
#     is_approved = BooleanField(default=None, null=True, blank=True, verbose_name='Одобрено')
#
#     class Meta:
#         verbose_name = 'Лабораторная работа'
#         verbose_name_plural = 'Лабораторные работы'
#
#     def __str__(self):
#         return (f"{self.name}. "
#                 f"Студент: {self.student}. "
#                 f"Одобрено: {self.is_approved}")
#
# ############
# from rest_framework.serializers import ModelSerializer
# from ..models.works import Work
# from rest_framework import serializers
# from student.models import StudentWork
#
#
# class BaseWorkSerializer(ModelSerializer):
#     """
#     Базовый сериалайзер реагенты
#     """
#
#     class Meta:
#         model = Work
#         fields = '__all__'
#
#
# from django.db.models import Model, ForeignKey, TextField, CharField, BooleanField
# from django.db.models.deletion import CASCADE
# from clients.models.client import ClientSystem
# from research.models import Research
#
#
# class Work(Model):
#     name = CharField(max_length=100, verbose_name='Наименование')
#     description = TextField(null=True, blank=True, verbose_name='Описание')
#     student = ForeignKey(to=ClientSystem, on_delete=CASCADE, related_name='student', verbose_name='Студент')
#     accept_person = ForeignKey(to=ClientSystem, on_delete=CASCADE, default=None, blank=True, null=True,
#                                related_name='accept_persons', verbose_name='Согласующий')
#     research = ForeignKey(to=Research, on_delete=CASCADE, related_name='works', verbose_name='Исследование',
#                           default=None)
#     is_approved = BooleanField(default=None, null=True, blank=True, verbose_name='Одобрено')
#
#     class Meta:
#         verbose_name = 'Лабораторная работа'
#         verbose_name_plural = 'Лабораторные работы'
#
#     def __str__(self):
#         return (f"{self.name}. "
#                 f"Студент: {self.student}. "
#                 f"Одобрено: {self.is_approved}")
#
#
# from rest_framework.viewsets import ModelViewSet
# from clients.permissions import IsTeacherPermission, IsStudentPermission
# from utils.paginations import SelectorPagination
# from ..models.works import Work
# from ..serializers.works import BaseWorkSerializer, BaseWorkStudentSerializer, WorkTeacherApproveSerializer, \
#     WorkStudentApproveSerializer
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status
# from utils.serializers import ACTIONS
#
#
# class WorksModelViewSet(
#     ModelViewSet,
# ):
#     """
#     ViewSet для взаимодействия с лабораторками
#
#     Присутствует пагинация с максимальным размером страницы 100 и значением по умолчанию 10
#     """
#     queryset = Work.objects.all()
#     serializer_class = BaseWorkSerializer
#     permission_classes = [
#         IsTeacherPermission
#     ]
#     pagination_class = SelectorPagination
#
#
# class WorkTeacherModelViewSet(
#     ModelViewSet
# ):
#     queryset = Work.objects.all()
#     serializer_class = BaseWorkSerializer
#     serializers_class = {
#         ACTIONS.POST: BaseWorkSerializer,
#
#     }
#     permission_classes = [
#         IsTeacherPermission
#     ]
#     pagination_class = SelectorPagination
#
#     @action(methods=['POST'], detail=True, url_path='approve')
#     def approve(self, request, *args, **kwargs):
#         object = self.get_object()
#         serializer = WorkTeacherApproveSerializer(
#             instance=object,
#             data={'is_approved': True}
#         )
#         serializer.is_valid()
#         serializer.update(serializer.instance, serializer.validated_data)
#         return Response(
#             status=status.HTTP_200_OK,
#             data=serializer.data
#         )
#
#
# class WorkStudentModelViewSet(
#     ModelViewSet
# ):
#     queryset = Work.objects.all()
#     serializer_class = BaseWorkStudentSerializer
#     serializers_class = {
#         ACTIONS.POST: BaseWorkStudentSerializer,
#     }
#     permission_classes = [
#         IsStudentPermission
#     ]
#     pagination_class = SelectorPagination
#
#     def get_queryset(self):
#         return super().get_queryset().filter(
#             student=self.request.user.client
#         )
#
#     @action(methods=['POST'], detail=True, url_path='send/to/approve')
#     def send_to_approve(self, request, *args, **kwargs):
#         object = self.get_object()
#         serializer = WorkStudentApproveSerializer(
#             instance=object,
#             data={'is_approved': False}
#         )
#         serializer.is_valid()
#         serializer.update(serializer.instance, serializer.validated_data)
#         return Response(
#             status=status.HTTP_200_OK,
#             data=serializer.data
#         )
#
#
# class WorkAssistantModelViewSet(
#     ModelViewSet
# ):
#     queryset = Work.objects.all()
#     serializer_class = BaseWorkSerializer
#     serializers_class = {
#         ACTIONS.POST: BaseWorkSerializer,
#     }
#     permission_classes = [
#         IsTeacherPermission
#     ]
#     pagination_class = SelectorPagination
#
#     @action(methods=['POST'], detail=True, url_path='take')
#     def date(self, request, *args, **kwargs):
#         object = self.get_object()
#         serializer = BaseWorkSerializer
#         instance = object
#         # data = {: True} сидел и думал как это сделать
#         serializer.is_valid()
#         serializer.save(serializer.validated_data)
#         return Response(
#             status=status.HTTP_200_OK,
#             data=serializer.data
#         )
#
#
# from django.urls import path, include
# from rest_framework.routers import SimpleRouter
# from .views.reagents import ReagentsModelViewSet, WorkReagentsModelViewSet, UnitsTypeView
# from .views.works import WorksModelViewSet, WorkStudentModelViewSet, WorkTeacherModelViewSet
# from .views.equipment import EquipmentModelViewSet
# from .views.result import ResultModelViewSet
# from .views.extra_fields import ExtraFieldsModelViewSet
# from .views.value_extra_fields import ValueModelViewSet
# from .views.equipment_drymethod import EquipmentDryMethodModelViewSet
#
# inventory_router = SimpleRouter()
# inventory_router.register(prefix='reagents', viewset=ReagentsModelViewSet, basename='reagents')
# inventory_router.register(prefix='works', viewset=WorksModelViewSet, basename='works')
#
# work_reagents_router = SimpleRouter()
# work_reagents_router.register(prefix='reagents', viewset=WorkReagentsModelViewSet, basename='work|reagents')
#
# equipment_router = SimpleRouter()
# equipment_router.register(prefix='equipments', viewset=EquipmentModelViewSet, basename='equipments')
#
# result_router = SimpleRouter()
# result_router.register(prefix='result', viewset=ResultModelViewSet, basename='work|result')
#
# extra_field_router = SimpleRouter()
# extra_field_router.register(prefix='extra_field', viewset=ExtraFieldsModelViewSet, basename='extra_field')
#
# value_extra_field_router = SimpleRouter()
# value_extra_field_router.register(prefix='value', viewset=ValueModelViewSet, basename='value') \
#  \
#     dry_method_router = SimpleRouter()
# dry_method_router.register(prefix='dry_method', viewset=EquipmentDryMethodModelViewSet, basename='dry_method')
#
# student_router = SimpleRouter()
# student_router.register(prefix='work', viewset=WorkStudentModelViewSet, basename='student|works')
#
# teacher_router = SimpleRouter()
# teacher_router.register(prefix='work', viewset=WorkTeacherModelViewSet, basename='teacher|works')
#
# urlpatterns = [
#     path('', include(inventory_router.urls)),
#     path('works/<int:work_id>/', include(work_reagents_router.urls)),
#     path('units/type/', view=UnitsTypeView.as_view(), name='units|type'),
#     path('', include(equipment_router.urls)),
#     path('', include(result_router.urls)),
#     path('', include(extra_field_router.urls)),
#     path('', include(value_extra_field_router.urls)),
#     path('', include(dry_method_router.urls)),
#     path('student/', include(student_router.urls)),
#     path('teacher/', include(teacher_router.urls)),
# ]
