from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    community_score = models.FloatField()
    seats = models.ManyToManyField("RideFeedback.Seat", through="RideFeedback.Booking")
