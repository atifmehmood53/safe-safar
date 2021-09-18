appModule.controller("LoginController", [
    "$scope", "$location",
    function($scope, $location) {
      $scope.username = '';
      $scope.password = '';


      $scope.login = function(){
        $location.path( "/preferences" )
      }    
    }
  ]);
  