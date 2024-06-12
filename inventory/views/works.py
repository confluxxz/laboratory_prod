from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsTeacherPermission, IsStudentPermission
from utils.paginations import SelectorPagination
from ..models.works import Work
from ..serializers.works import BaseWorkSerializer, BaseWorkStudentSerializer, WorkTeacherApproveSerializer, WorkStudentApproveSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from utils.serializers import ACTIONS

class WorksModelViewSet(
    ModelViewSet,
):
    """
    ViewSet для взаимодействия с лабораторками

    Присутствует пагинация с максимальным размером страницы 100 и значением по умолчанию 10
    """
    queryset = Work.objects.all()
    serializer_class = BaseWorkSerializer
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination



class WorkTeacherModelViewSet(
    ModelViewSet
):
    queryset = Work.objects.all()
    serializer_class = BaseWorkSerializer
    serializers_class = {
        ACTIONS.POST: BaseWorkSerializer,

    }
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination

    @action(methods=['POST'], detail=True, url_path='approve')
    def approve(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = WorkTeacherApproveSerializer(
            instance = object,
            data = {'is_approved': True}
        )
        serializer.is_valid()
        serializer.update(serializer.instance, serializer.validated_data)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )



class WorkStudentModelViewSet(
    ModelViewSet
):
    queryset = Work.objects.all()
    serializer_class = BaseWorkStudentSerializer
    serializers_class = {
        ACTIONS.POST: BaseWorkStudentSerializer,
    }
    permission_classes = [
        IsStudentPermission
    ]
    pagination_class = SelectorPagination

    def get_queryset(self):
        return super().get_queryset().filter(
            student=self.request.user.client
        )
    @action(methods=['POST'], detail=True, url_path='send/to/approve')
    def send_to_approve(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = WorkStudentApproveSerializer(
            instance = object,
            data = {'is_approved': False}
        )
        serializer.is_valid()
        serializer.update(serializer.instance, serializer.validated_data)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

class WorkAssistantModelViewSet (
    ModelViewSet
):
    queryset = Work.objects.all()
    serializer_class = BaseWorkSerializer
    serializers_class = {
        ACTIONS.POST: BaseWorkSerializer,
    }
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination

    @action(methods=['POST'], detail=True, url_path='take')
    def date(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = BaseWorkSerializer
        instance = object
        #data = {: True} сидел и думал как это сделать
        serializer.is_valid()
        serializer.save(serializer.validated_data)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
