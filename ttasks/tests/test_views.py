"""View tests da aplicação ttasks."""

from unittest import mock

from django.core import urlresolvers
from rest_framework import status, test

from .. import factories, models


class TaskAPITests(test.APITestCase):
    """Testa a api de tarefas."""

    @classmethod
    def setUpTestData(cls):
        """Class fixtures."""
        cls.tasks_api_url = urlresolvers.reverse('v1:task-list')
        super().setUpTestData()

    def test_task_create(self):
        """Verifica a criação de tarefas."""
        # inicialmente não há tarefas salvas.
        self.assertEqual(models.Task.objects.count(), 0)

        # usuário cria uma tarefa
        data = dict(title='Tarefa teste.')
        response = self.client.post(self.tasks_api_url, data)

        # a api executa com sucesso e uma tarefa é adicionada ao db
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(models.Task.objects.count(), 1)
        task = models.Task.objects.first()
        self.assertEqual(task.title, 'Tarefa teste.')

    def test_task_update(self):
        """Verifica a atualização de tarefas."""
        # tarefa a ser atualizada
        task = models.Task.objects.create(title='Tarefa para atualização.')
        self.assertEqual(models.Task.objects.count(), 1)

        # a api para atualização é utilizada com sucesso.
        data = dict(title='Tarefa atualizada.')
        response = self.client.put(urlresolvers.reverse('v1:task-detail', args=[task.pk]), data)
        self.assertTrue(status.is_success(response.status_code))

        # o objeto é atualizado com sucesso.
        self.assertEqual(models.Task.objects.count(), 1)
        task.refresh_from_db()
        self.assertEqual(str(task), 'Tarefa atualizada.')

    def test_completed_tasks(self):
        """Verifica se as tarefas com status completado são obtidas com sucesso."""
        # 2 tarefas completadas e 1 a completar são criadas
        models.Task.objects.create(title='Tarefa 1', completed=True)
        models.Task.objects.create(title='Tarefa 2', completed=True)
        models.Task.objects.create(title='Tarefa 3', completed=False)
        self.assertEqual(models.Task.objects.count(), 3)

        # utiliza a api para obter apenas tarefas completadas.
        data = dict(page_size=1)
        response = self.client.get(urlresolvers.reverse('v1:task-list') + 'completed/', data)
        self.assertTrue(status.is_success(response.status_code))
        tasks = response.data
        self.assertEqual(tasks['count'], 2)
        self.assertEqual(len(tasks['results']), 1)

    def test_completed_tasks_no_pagination(self):
        """Verifica a api com a paginação desligada."""
        # após a criação de várias tarefas completadas, a paginação é desligada na View.
        factories.TaskFactory.create_batch(20, completed=True)
        self.assertEqual(models.Task.objects.count(), 20)

        # a api não contém a resposta paginada.
        with mock.patch('ttasks.views.TaskAPI.pagination_class', None):
            response = self.client.get(urlresolvers.reverse('v1:task-list') + 'completed/')
            self.assertTrue(status.is_success(response.status_code))
            tasks = response.data
            self.assertTrue(len(tasks), 20)
