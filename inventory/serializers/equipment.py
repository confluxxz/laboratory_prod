from rest_framework.serializers import ModelSerializer
from ..models.equipment import Equipment

class BaseEquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
