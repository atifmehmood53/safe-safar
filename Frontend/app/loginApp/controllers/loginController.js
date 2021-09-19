appModule.controller("LoginController", [
    "$scope", "$location",
    function($scope, $location) {
      $scope.username = '';
      $scope.password = '';

      $scope.setSideBarState(true);

      $scope.login = function(){
        $location.path( "/preferences" )
        $scope.setSideBarState(false);
      }    
    }
  ]);
  