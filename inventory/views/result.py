from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsTeacherPermission
from utils.paginations import SelectorPagination
from ..models import Result
from ..serializers.result import BaseResultSerializer

class ResultModelViewSet (
    ModelViewSet,
):
    queryset = Result.objects.all()
    serializer_class = BaseResultSerializer
    permission_classes = [IsTeacherPermission]
    pagination_class = SelectorPagination
