from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsTeacherPermission, IsAssistantPermission
from utils.paginations import SelectorPagination
from ..models import DryMethod
from ..serializers.equipment_drymethod import BaseDryMethodSerializer
from rest_condition.permissions import Or

class EquipmentDryMethodModelViewSet (
    ModelViewSet,
):
    queryset = DryMethod.objects.all()
    serializer_class = BaseDryMethodSerializer
    permission_classes = [Or(
        IsTeacherPermission, IsAssistantPermission
    )]
    pagination_class = SelectorPagination
