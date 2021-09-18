from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Ride(models.Model):
    name = models.CharField(max_length=10)


class UserRide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    class Meta:
        unique_together = ("user", "ride")


class RidePalFeedback(models.Model):
    user_ride = models.ForeignKey(UserRide, on_delete=models.CASCADE)
    pal_ride = models.ForeignKey(UserRide, on_delete=models.CASCADE, related_name='pal_rides')

    NEUTRAL = 'neutral'
    DOWN = 'down'
    UP = 'up'
    BLACKLIST = 'blacklist'

    VOTE_CHOICES = (
        (NEUTRAL, 'neutral'),
        (DOWN, 'down'),
        (UP, 'up'),
        (BLACKLIST, 'blacklist')
    )
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES, default=NEUTRAL)

    class Meta:
        unique_together = ("user_ride", "pal_ride")

