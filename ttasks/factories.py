"""Fábricas da aplicação ttasks."""

import factory

from . import models


class TaskFactory(factory.django.DjangoModelFactory):
    """Fábrica de tarefas."""

    @factory.sequence
    def title(n):
        """Título aleatório."""
        return f'Tarefa {n}'

    class Meta:
        model = models.Task
