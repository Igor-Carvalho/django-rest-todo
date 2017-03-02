(function () {
  'use strict';
  
  angular.module('todo').factory('Task', ['$resource', resource]);

  function resource($resource) {
    var baseURL = '/api/v1/tasks/';

    function buildTask(task) {
      return new Task(task);
    }

    function setupTasks(response) {
      var tasks = angular.fromJson(response);
      var results = [];
      angular.forEach(tasks.results, function (task) {
        results.push(buildTask(task));
      });
      tasks.results = results;
      return tasks;
    }

    var Task = $resource(baseURL + ':id/', {id: '@id'}, {
      query: {
        method: 'GET',
        isArray: false,
        transformResponse: function (response) {
          return setupTasks(response);
        }
      },
      update: {
        method: 'PUT'
      },
      completas: {
        method: 'GET',
        url: baseURL + 'completed/',
        isArray: false,
        transformResponse: function (response) {
          return setupTasks(response);
        }
      }
    });

    Task.buildTask = buildTask;
    Task.setupTasks = setupTasks;
    return Task;
  }
})();
