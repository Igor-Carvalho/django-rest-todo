(function () {
  'use strict';
  
  angular.module('todo')
    .config(['$interpolateProvider', interpolateConfig])
    .config(['$resourceProvider', resourceConfig])
    .config(['$compileProvider', compileConfig]);

  function interpolateConfig($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }

  function resourceConfig($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
  }

  function compileConfig($compileProvider) {
    $compileProvider.debugInfoEnabled(false);
    $compileProvider.commentDirectivesEnabled(false);
    $compileProvider.cssClassDirectivesEnabled(false);
  }
})();
