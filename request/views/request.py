from rest_framework.viewsets import ModelViewSet

from clients.permissions import IsTeacherPermission, IsAssistantPermission
from utils.paginations import SelectorPagination
from ..models import Request
from ..serializers.request import BaseRequestSerializer
from rest_condition.permissions import Or


class RequestModelViewSet (
    ModelViewSet,
):
    queryset = Request.objects.all()
    serializer_class = BaseRequestSerializer
    permission_classes = [Or(
        IsTeacherPermission,
        IsAssistantPermission
    )]
    pagination_class = SelectorPagination
