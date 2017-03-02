"""Serializadores da aplicação tasks."""

from rest_framework import serializers

from . import models


class TaskSerializer(serializers.ModelSerializer):
    """Serializador de tarefas."""

    class Meta:
        model = models.Task
        fields = ['id', 'title', 'completed']
        extra_kwargs = {
            'title': {
                'min_length': 5
            }
        }
