(function () {
  'use strict';
  
  angular.module('todo').component('paginator', {
    templateUrl: ['paginatorTemplate', function (paginatorTemplate) { return paginatorTemplate;}],
    controllerAs: 'vm',
    bindings: {
      data: '=',
      loader: '=',
      pageSize: '=',
      search: '='
    }
  });
})();
