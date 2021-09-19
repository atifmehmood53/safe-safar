appModule.controller("preferencesController", [
    "$scope", "$location", "$timeout", 'userPreferenceService',
    function($scope, $location, $timeout, userPreferenceService) {
      $scope.fetchingPreferences = true;
      $scope.preferenceFields = []

      $scope.fetchPreferencesQuestions = function(){
        $scope.fetchingPreferences = true;
        userPreferenceService.fetchPreferencesQuestions(function(data){
          $scope.preferenceFields = data;
          $scope.fetchingPreferences = false;
        },function(){
          $scope.fetchingPreferences = false;
        })
      }
  
  
      $scope.submitPreferences = function(){
        $scope.submittingPrefences = true;
        
        feedbackService.savePreferences({
          answers: $scope.preferenceFields.map(field => field.value)
        },function(){
          // success
          $scope.submittingPrefences = false; 
          $location.path( "/home" )
        }, function(){
          //error 
          $scope.submittingPrefences = false;   
        })
        $timeout(function(){
          $scope.submittingPrefences = false;
          $location.path( "/home" )
        }, 5000)
      }
    }
  ]);
  