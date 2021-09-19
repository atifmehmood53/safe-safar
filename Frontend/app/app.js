let appModule = angular.module("app", ['ngRoute']);
let PORT = 10000
let BASE_URL = `http://127.0.0.1:${PORT}`
let userId = 1;
let postHeaders = {
  "Content-Type": "application/json"
}


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