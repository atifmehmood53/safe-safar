appModule.controller("feedbackController", [
    "$scope", "$location",
    function($scope, $location) {
      $scope.selectedVotes = {};

      $scope.voteMap = {
        'up-vote': {
          icon: 'bi-hand-thumbs-up-fill text-success',
          label: 'up voted'
        },
        'down-vote': {
          icon: 'bi-hand-thumbs-down-fill',
          label: 'down voted'
        },
        'red-flag': {
          icon: ' bi-flag-fill text-danger',
          label: 'red flaged'
        },
      }

      $scope.getLengthOfSelectedVotes = function(){
        return Object.keys($scope.selectedVotes).length;
      }

      $scope.changeVote = function(vote, seatNumber){
        console.log("seat", vote, seatNumber)
        if ($scope.selectedVotes[seatNumber] == vote){
          delete $scope.selectedVotes[seatNumber];
        }else{
          $scope.selectedVotes[seatNumber] = vote;
        }
      }
    }
  ]);
  