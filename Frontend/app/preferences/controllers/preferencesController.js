appModule.controller("preferencesController", [
    "$scope", "$location", "$timeout", 'userPreferenceService',
    function($scope, $location, $timeout, userPreferenceService) {
      $scope.fetchingPreferences = true;
      $scope.preferenceFields = []

      $scope.fetchPreferencesQuestions = function(){
        $scope.fetchingPreferences = true;
        userPreferenceService.fetchPreferencesQuestions(function(data){
          $scope.preferenceFields = data;
          userPreferenceService.fetchUserPreferences(function(data){
            console.log(data)
            $scope.fetchingPreferences = false;
          }, function(){
            $scope.fetchingPreferences = false;
          })
        },function(){
          $scope.fetchingPreferences = false;
        })
      }
  
  
      $scope.submitPreferences = function(){
        $scope.submittingPrefences = true;
        
        userPreferenceService.savePreferences({
          customer_id: userId, 
          answers: $scope.preferenceFields.map(function(field){
            if (field && field.value && field.value.id){
              return field.value.id
            }
          })
        },function(){
          // success
          $scope.submittingPrefences = false; 
          $scope.showSuccessMessage("Your preferences were saved sucessfully!")
          $location.path( "/home" )
        }, function(){
          //error 
          $scope.submittingPrefences = false;   
        })
      }


      $scope.fetchPreferencesQuestions();
    }
  ]);
  