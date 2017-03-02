(function () {
  'use strict';
  
  angular.module('todo').directive('tasks', ['tasksTemplate', tasks]);

  function tasks(tasksTemplate) {
    return {
      restrict: 'E',
      templateUrl: tasksTemplate,
      controllerAs: 'vm',
      controller: ['Task', 'toastr', controller]
    }

    function controller(Task, toastr) {
      var self = this;
      self.$onInit = onInit;
      self.loadTasks = loadTasks;
      self.loadCompletedTasks = loadCompletedTasks;
      self.createTask = createTask;
      self.updateTask = updateTask;
      self.updateTaskInput = updateTaskInput;
      self.deleteTask = deleteTask;

      function onInit() {
        self.task = {};
        self.pageSize = 5;
        self.loadTasks({page_size: self.pageSize});
      }

      function loadTasks(params) {
        self.loader = loadTasks;
        self.tasksPromise = Task.query(params, success).$promise;

        function success(tasks) {
          self.tasks = tasks;
        }
      }

      function loadCompletedTasks(params) {
        self.loader = loadCompletedTasks;
        self.tasksPromise = Task.completas(params, success).$promise;

        function success(tasks) {
          self.tasks = tasks;
        }
      }

      function createTask() {
        self.errors = {};
        self.promise = new Task(self.task).$save(success, error);

        function success(task) {
          self.task = {};
          self.loadTasks({page_size: self.pageSize});
          toastr.success('Tarefa criada com sucesso.');
        }

        function error(response) {
          self.errors = response.data;
        }
      }

      function updateTask(task) {
        self.updateTaskError = null;
        task.__promise = task.$update(success, error);

        function success(task) {
          toastr.success('Tarefa #' + task.id + ' atualizada com sucesso');
        }

        function error(response) {
          self.updateTaskError = {
            task: task,
            errors: response.data
          };
          toastr.error('Erro ao atualizar tarefa');
          return task.$get();
        }
      }

      function updateTaskInput($event, task) {
        if ($event.which === 13) {
          updateTask(task);
          task.__showInput = false;
        }
      }

      function deleteTask(task) {
        if (confirm('Confirma deleção da tarefa '+ task.title + '?')) {
          self.tasksPromise = task.$delete(function (task) {
            self.loadTasks({page_size: self.pageSize});
            toastr.success('Tarefa removida com sucesso.');
          });
        }
      }
    }
  }
})();
