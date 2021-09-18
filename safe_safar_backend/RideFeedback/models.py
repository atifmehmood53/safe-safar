from django.db import models


# Create your models here.
from safe_safar_backend.Preference.models import Customer


class Ride(models.Model):
    name = models.CharField(max_length=10)


class Seat(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)


class CustomerSeat(models.Model):
    pass


class CustomerSeats(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat, through=CustomerSeat)


class PalFeedback(models.Model):
    customer_seat = models.ForeignKey(CustomerSeat, on_delete=models.CASCADE)
    pal_seat = models.ForeignKey(CustomerSeats, on_delete=models.CASCADE, related_name='pal_seats')

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
        unique_together = ("customer_seat", "pal_seat")


class CustomersMatchScore(models.Model):
    pal1 = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pal2 = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pal2')
    score1 = models.DecimalField(max_length=10)  # pal 1 scores pal 2
    score2 = models.DecimalField(max_length=10)  # pal 2 scores pal 1
