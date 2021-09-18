from django.db import models


# Create your models here.
class Ride(models.Model):
    name = models.CharField(max_length=10)


class Seat(models.Model):
    ride = models.ForeignKey("Ride", on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)


class Booking(models.Model):
    customer = models.ForeignKey("Preference.Customer", on_delete=models.CASCADE)
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE)


class CustomersMatchScore(models.Model):
    pal1 = models.ForeignKey("Preference.Customer", on_delete=models.CASCADE)
    pal2 = models.ForeignKey("Preference.Customer", on_delete=models.CASCADE, related_name='pal2')
    score1 = models.DecimalField(decimal_places=3, max_digits=7)  # pal 1 scores pal 2
    score2 = models.DecimalField(decimal_places=3, max_digits=7)  # pal 2 scores pal 1


class PalFeedback(models.Model):
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    pal_booking = models.ForeignKey("Booking", on_delete=models.CASCADE, related_name='pal_booking')

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
        unique_together = ("booking", "pal_booking")
