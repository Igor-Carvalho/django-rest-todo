"""Modelos da aplicação tasks."""

from django.db import models

from . import managers


class Task(models.Model):
    """Uma tarefa."""

    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    objects = managers.TaskManager()

    def __str__(self):
        """toString."""
        return self.title

    class Meta:
        ordering = ['-id']
