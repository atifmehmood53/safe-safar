appModule.controller("feedbackController", [
    "$scope", "$location", "feedbackService",
    function($scope, $location, feedbackService) {
      let availableSeats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
      $scope.selectedVotes = {};

      $scope.voteMap = {
        'up-vote': {
          icon: 'bi-hand-thumbs-up-fill text-success',
          label: 'up voted',
          value: '1.3'
        },
        'down-vote': {
          icon: 'bi-hand-thumbs-down-fill',
          label: 'down voted',
          value: '0.8'
        },
        'red-flag': {
          icon: ' bi-flag-fill text-danger',
          label: 'red flaged',
          value: '0.0'
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

      $scope.submitFeedBack = function(){
        let data = {
          customer_id: userId,
          seat_votes: availableSeats.map(function(seat){
            return {
              seat: seat,
              vote: $scope.selectedVotes[seat] ? $scope.voteMap[$scope.selectedVotes[seat]].value : '0.0'
            }
          })
        }

        feedbackService.submitFeedBack(data, function(){
          // success 
          $scope.showSuccessMessage("Your feedback was saved sucessfully!")
        }, function(){

        })
      }
    }
  ]);
  