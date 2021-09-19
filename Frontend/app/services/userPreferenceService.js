calendarModule.service("userPreferenceService", [
  "$http",
  function($http) {
    let url = `${BASE_URL}/`
    $scope.fetchPreferences = function(successCallBack, errorCallBack){
      $http.get(url).then(
        response => {
          if (response.status === 200) {
            onSuccess(response.data);
            this.fetchTennant();
          } else {
            onError(response.data);
            this.fetchTennant();
          }
        },
        err => {
          onError("Some unexpected Error occured");
          this.fetchTennant();
        }
      );
    }

    $scope.fetchPreferencesQuestions = function(successCallBack, errorCallBack){
      $http.get(url).then(
        response => {
          if (response.status === 200) {
            onSuccess(response.data);
            this.fetchTennant();
          } else {
            onError(response.data);
            this.fetchTennant();
          }
        },
        err => {
          onError("Some unexpected Error occured");
          this.fetchTennant();
        }
      );
    }


    $scope.savePreferences = function(data, successCallBack, errorCallBack){
      let url = `${BASE_URL}/`
      $http.post(url, data).then(
        response => {
          if (response.status === 200) {
            if (typeof(successCallBack) === "function"){
              successCallBack(response.data);
            }
          
          } else {
            if (typeof(errorCallBack) === "function"){
              errorCallBack("Some unexpected Error occured");
            }
          }
        },
        err => {
          if (typeof(errorCallBack) === "function"){
            errorCallBack("Some unexpected Error occured");
          }
        }
      );
    }
  }
]);
