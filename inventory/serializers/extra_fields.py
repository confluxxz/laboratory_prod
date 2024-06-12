from rest_framework.serializers import ModelSerializer
from ..models.extra_fields import ExtraFields
class BaseExtraFieldsSerializer(ModelSerializer):
    class Meta:
        model = ExtraFields
        fields = '__all__'
