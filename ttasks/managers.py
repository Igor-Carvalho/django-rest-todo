"""Managers da aplicação tasks."""

from django.db import models


class TaskManager(models.Manager):
    """Gerenciador de tarefas."""

    def tarefas_completadas(self):
        """Obtém tarefas completadas."""
        return self.model.objects.filter(completed=True)
