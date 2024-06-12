from rest_framework.serializers import ModelSerializer
from ..models.equipment_drymethod import DryMethod
class BaseDryMethodSerializer(ModelSerializer):
    class Meta:
        model = DryMethod
        fields = '__all__'
