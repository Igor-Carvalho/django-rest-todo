"""
Remove todas as tarefas do banco do dados.

Idealmente, esse comando deveria ser executado toda 00:00:00 via cronjob para limpar o banco de dados.
"""

import logging

from django.core import management

from ... import models

logger = logging.getLogger(__name__)


class Command(management.BaseCommand):
    """Comando."""

    def handle(self, **options):
        """Executa o comando."""
        logger.info('limpando tarefas...')
        results = models.Task.objects.all().delete()
        msg = f'{results[1].get("ttasks.Task", 0)} tarefa(s) removida(s) com sucesso.'
        logger.info(msg)
