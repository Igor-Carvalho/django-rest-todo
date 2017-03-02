"""Verifica os comandos da aplicaçao ttasks."""

from django import test
from django.core import management

from .. import factories, models


class CommandTest(test.TestCase):
    """Testa comandos."""

    def test_wipe_tasks(self):
        """Verifica se as tarefas são removidas com sucesso."""
        # 20 tarefas são criadas.
        factories.TaskFactory.create_batch(20)
        self.assertEqual(models.Task.objects.count(), 20)

        # o comando é executado e as tarefas são removidas com sucesso.
        management.call_command('wipe_tasks')
        self.assertEqual(models.Task.objects.count(), 0)
