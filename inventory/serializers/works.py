from rest_framework.serializers import ModelSerializer
from ..models.works import Work
from rest_framework import serializers
from student.models import StudentWork

class BaseWorkSerializer(ModelSerializer):
    """
    Базовый сериалайзер реагенты
    """
    class Meta:
        model = Work
        fields = '__all__'


class BaseWorkStudentSerializer(BaseWorkSerializer):
    is_approved = serializers.BooleanField(read_only=True)

class WorkTeacherApproveSerializer(BaseWorkSerializer):
    class Meta(BaseWorkSerializer.Meta):
        fields = ('is_approved',)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        student_work = StudentWork.objects.create(student=instance.student, work=instance)


class WorkStudentApproveSerializer(BaseWorkSerializer):
    class Meta(BaseWorkSerializer.Meta):
        fields = ('is_approved',)
