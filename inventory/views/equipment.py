from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsTeacherPermission, IsAssistantPermission
from utils.paginations import SelectorPagination
from ..models import Equipment
from ..serializers.equipment import BaseEquipmentSerializer
from rest_condition.permissions import Or

class EquipmentModelViewSet (
    ModelViewSet,
):
    queryset = Equipment.objects.all()
    serializer_class = BaseEquipmentSerializer
    permission_classes = [Or(
        IsTeacherPermission, IsAssistantPermission
    )]
    pagination_class = SelectorPagination
