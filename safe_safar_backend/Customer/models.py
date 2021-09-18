from django.contrib.auth.models import User


class Customer(User):
    community_score = models.FloatField()
