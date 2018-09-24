from rest_framework import serializers
from todo_list.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'created', 'name', 'description', 'completed')

