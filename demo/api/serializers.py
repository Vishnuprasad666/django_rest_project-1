from rest_framework import serializers
from api.models import Teacher

class AssignmentSerializer(serializers.Serializer):
    title=serializers.CharField()
    description=serializers.CharField()
    last_date=serializers.DateField()

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"