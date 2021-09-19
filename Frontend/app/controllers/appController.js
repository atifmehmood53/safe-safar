appModule.controller("AppController", [
  "$scope", "$location", "$timeout",
  function($scope, $location, $timeout) {
    $scope.hideSideBar = false;

    $scope.setSideBarState = function(shouldShow) {
      $scope.hideSideBar = shouldShow;
    }


    $scope.showSuccessMessage = function(message){
      console.log(message)
      $scope.message = message;
      $timeout(function(){
        $scope.message = ""
      }, 5000)
    }

    $scope.navigateToState = function(state) {
      if (state === 'feedback'){
        $location.path( "/feedback" )
      }else if (state === 'preferences'){
        $location.path( "/preferences" )
      }
      else if (state === 'home'){
        $location.path( "/home" )
        $scope.hideSideBar = false;
      }
      else if (state === 'login'){
        $location.path( "/" )
        $scope.hideSideBar = true;
      }
      $scope.closeNav()
    }

    /* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
    $scope.openNav = function() {
      document.getElementById("sidebar").style.width = "500px";
    }

    /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
    $scope.closeNav = function() {
      document.getElementById("sidebar").style.width = "0";
    }
  }
]);
