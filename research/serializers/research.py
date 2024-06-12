from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import Research

class BaseResearchSerializer(ModelSerializer):

    student = SerializerMethodField()
    class Meta:
        model = Research
        fields = '__all__'

    def get_student(self, obj):
        return {
            "uuid": obj.student.uuid,
            "student": str(obj.student),
            "group": obj.student.group
        }