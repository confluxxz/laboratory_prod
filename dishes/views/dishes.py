from rest_framework.viewsets import ModelViewSet

from clients.permissions import IsTeacherPermission
from utils.paginations import SelectorPagination
from ..models import Dishes
from ..serializers import (DishesListModelSerializer,
                           DishesDetailModelSerializer,
                           DishesCreateModelSerializer,)

class DishesModelViewSet (
    ModelViewSet,
):
    queryset = Dishes.objects.all()
    serializer_class = DishesListModelSerializer
    permission_classes = [
        IsTeacherPermission
    ]
    pagination_class = SelectorPagination
    serializer_classes = {
        "list":DishesListModelSerializer,
        "detail":DishesDetailModelSerializer,
        "create":DishesCreateModelSerializer,
        "update":DishesCreateModelSerializer,
    }

