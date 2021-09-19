appModule.service("userPreferenceService", [
  "$http",
  function($http) {
    let userPreferenceService = this;
  
    userPreferenceService.fetchUserPreferences = function(successCallBack, errorCallBack){
      let url = `${BASE_URL}/preference/retrieve_preferences?customer_id=${userId}`
    
      $http.get(url).then(
        response => {
          if (response.status === 200) {
            successCallBack(response.data);
          } else {
            errorCallBack(response.data);
          }
        },
        err => {
          errorCallBack("Some unexpected Error occured");
        }
      );
    }

    userPreferenceService.fetchPreferencesQuestions = function(successCallBack, errorCallBack){
      let url = `${BASE_URL}/preference/preference_questions`
      $http.get(url).then(
        response => {
          if (response.status === 200) {
            successCallBack(response.data);
          } else {
            onError(response.data);
          }
        },
        err => {
          errorCallBack("Some unexpected Error occured");
        }
      );
    }


    userPreferenceService.savePreferences = function(data, successCallBack, errorCallBack){
      let url = `${BASE_URL}/preference/submit_preferences`
      $http.post(url, data, {
        headers: postHeaders,
      }).then(
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
