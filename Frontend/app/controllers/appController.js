appModule.controller("AppController", [
  "$scope",
  function($scope) {
  
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
