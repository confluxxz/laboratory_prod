from rest_framework.serializers import ModelSerializer
from ..models.result import Result
class BaseResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
