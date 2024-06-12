from rest_framework.viewsets import ModelViewSet
from utils.paginations import SelectorPagination
from ..models import ExtraFields
from ..serializers.extra_fields import BaseExtraFieldsSerializer

class ExtraFieldsModelViewSet (
    ModelViewSet,
):
    queryset = ExtraFields.objects.all()
    serializer_class = BaseExtraFieldsSerializer
    pagination_class = SelectorPagination
