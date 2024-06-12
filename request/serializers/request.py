from rest_framework.serializers import ModelSerializer
from ..models import Request

class BaseRequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
