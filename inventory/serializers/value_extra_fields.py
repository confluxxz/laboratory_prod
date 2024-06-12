from rest_framework.serializers import ModelSerializer
from ..models.value_extra_fields import Value
class BaseValueSerializer(ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'
