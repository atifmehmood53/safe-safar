from django.contrib.auth.models import User
from django.db import models


class CustomerPreferenceAnswer(models.Model):
    user = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
    preference_answers = models.ManyToManyField("PreferenceAnswer")


class PreferenceQuestion(models.Model):
    BOOL = 'bool'
    CHECK = 'check'
    DROP_DOWN = 'drop down'

    TYPE_CHOICES = (
        (
            (BOOL, 'bool'),
            (CHECK, 'check'),
            (DROP_DOWN, 'drop_down')
        )
    )

    question = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DROP_DOWN)


class PreferenceAnswer(models.Model):
    preference_question = models.ForeignKey("PreferenceQuestion", on_delete=models.CASCADE)
    answer = models.CharField(max_length=10)

    class Meta:
        unique_together = ['preference_question', 'answer']
