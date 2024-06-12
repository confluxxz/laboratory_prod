from rest_framework.viewsets import ModelViewSet
from clients.permissions import IsAssistantPermission
from utils.paginations import SelectorPagination
from ..models import Research
from ..serializers import BaseResearchSerializer

class ResearchModelViewSet (
    ModelViewSet,
):
    queryset = Research.objects.all()
    serializer_class = BaseResearchSerializer
    permission_classes = [
        IsAssistantPermission
    ]
    pagination_class = SelectorPagination
