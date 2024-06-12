from rest_framework.serializers import ModelSerializer
from ..models import Dishes
from rest_framework.exceptions import ValidationError


class BaseDishesSerializer(ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'


class DishesListModelSerializer(BaseDishesSerializer):

    class Meta(BaseDishesSerializer.Meta):
        fields = None
        exclude = ['last_update_date']


class DishesDetailModelSerializer(DishesListModelSerializer):

    class Meta(DishesListModelSerializer.Meta):
        exclude = ['last_update_date']


class DishesCreateModelSerializer(BaseDishesSerializer):

    class Meta(BaseDishesSerializer.Meta):
        fields = None
        read_only_fields = ['dishes']
