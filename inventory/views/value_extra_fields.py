from rest_framework.viewsets import ModelViewSet
from utils.paginations import SelectorPagination
from ..models import Value
from ..serializers.value_extra_fields import BaseValueSerializer


class ValueModelViewSet (
    ModelViewSet,
):
    queryset = Value.objects.all()
    serializer_class = BaseValueSerializer
    pagination_class = SelectorPagination
