from decimal import Decimal

from django.db import models


# Create your models here.
class Ride(models.Model):
    name = models.CharField(max_length=10)


class Seat(models.Model):
    ride = models.ForeignKey("Ride", on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)


class Booking(models.Model):
    customer = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE)
    # datetime

    class Meta:
        # TODO: Unique with datetime
        unique_together = ("customer", "seat")

    def provide_feedback_to_booking(self, another_booking, vote):
        pf = PalFeedback.objects.create(booking=self, pal_booking=another_booking, vote=vote)
        cms, _ = CustomersMatchScore.objects.get_or_create(pal_1=self.customer, pal_2=another_booking.customer)
        cms.update_score_with_vote(pf.vote)
        another_booking.update_community_score()

    def update_community_score(self):
        self.customer.update_community_score(self.pal_feedback.all())


class CustomersMatchScore(models.Model):
    pal_1 = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
    pal_2 = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE, related_name='pal2')
    score = models.DecimalField(decimal_places=3, max_digits=7, default=Decimal('1.000'))  # pal 1 scores pal 2

    def update_score_with_vote(self, vote):
        self.score *= Decimal(vote)
        self.save(update_fields=['score'])


class PalFeedback(models.Model):
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    pal_booking = models.ForeignKey("Booking", on_delete=models.CASCADE, related_name='pal_feedback')

    NEUTRAL = '1.0'
    DOWN = '0.8'
    UP = '1.3'
    BLACKLIST = '0.0'

    VOTE_CHOICES = (
        (NEUTRAL, 'neutral'),
        (DOWN, 'down'),
        (UP, 'up'),
        (BLACKLIST, 'blacklist')
    )
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES, default=NEUTRAL)

    class Meta:
        unique_together = ("booking", "pal_booking")
