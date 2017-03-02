"""Views da aplicação tasks."""

from django.views import generic
from rest_framework import decorators, response, viewsets

from . import models, pagination, serializers


class TasksView(generic.TemplateView):
    """Página de tarefas."""

    template_name = 'tasks/index.html'


tasks = TasksView.as_view()


class TaskAPI(viewsets.ModelViewSet):
    """Tasks API."""

    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    pagination_class = pagination.CorePaginator

    @decorators.list_route()
    def completed(self, request):
        """Obtém tarefas que foram marcadas como completas."""
        queryset = models.Task.objects.tarefas_completadas()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
