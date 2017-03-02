"""Administração da aplicação tasks."""

from django.contrib import admin

from . import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    """Configuração de tasks na interface admin."""
