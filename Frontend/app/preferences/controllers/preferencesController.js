appModule.controller("preferencesController", [
    "$scope", "$location",
    function($scope, $location) {
      $scope.preferenceFields = [
        {
          question: "Radio asgasga sashas asahsa sashas asgas asgasa sasgas asgas asgas asgasa s",
          type: "bool",
          options: [{value: "yes", id: "asasas"}, {value: "no", id: "assaassa"}]
        },
        {
          question: "Radio asgasga sashas asahsa sashas asgas asgasa sasgas asgas asgas asgasa s",
          type: "check",
          options: [{value: "yes", id: "asasas"}, {value: "no", id: "assaassa"}]
        },
        {
          question: "Radio asgasga sashas asahsa sashas asgas asgasa sasgas asgas asgas asgasa s",
          type: "dropdown",
          options: [{value: "yes", id: "asasas"}, {value: "no", id: "assaassa"}]
        },
      ]
    }
  ]);
  