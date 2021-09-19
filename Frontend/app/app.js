var appModule = angular.module("app", ['ngRoute']);

appModule.config(function($routeProvider) {
    $routeProvider
    .when("/", {
      templateUrl : "./loginApp/templates/login.html",
      controller: "LoginController"
    })
    .when("/preferences", {
      templateUrl : "./preferences/templates/preferences.html",
      controller: "preferencesController"
    })
});