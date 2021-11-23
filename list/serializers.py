from rest_framework import serializers
from django.utils import timezone
from . models import List, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'completed', 'parent_list', 'priority')

    def validate_deadline(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value

class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ('id','title', 'tasks')