from rest_framework import serializers
from api.models import Teacher,Todo

class AssignmentSerializer(serializers.Serializer):
    title=serializers.CharField()
    description=serializers.CharField()
    last_date=serializers.DateField()

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"
        
class TodoSerializer(serializers.Serializer):
    class Meta:
        model=Todo
        fields="__all__"
        read_only=["created_at","status"]
    
    def validate(self, attrs):
        title_val=attrs.get('title')
        if len(title_val)<5:
            raise serializers.ValidationError("Title should be atleast 5 characters in length!")
        return super().validate(attrs)