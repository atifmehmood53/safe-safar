appModule.service("feedbackService", [
  "$http",
  function($http) {
    let feedbackService = this;
  
    feedbackService.submitFeedBack= function(data, successCallBack, errorCallBack){
      let url = `${BASE_URL}/RideFeedback/submit_feedback`
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
