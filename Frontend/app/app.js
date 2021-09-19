let appModule = angular.module("app", ['ngRoute']);
let BASE_URL

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
    .when("/feedback", {
      templateUrl : "./feedback/templates/feedback.html",
      controller: "feedbackController"
    })
    .when("/home", {
      templateUrl : "./templates/home.html"
    })
});