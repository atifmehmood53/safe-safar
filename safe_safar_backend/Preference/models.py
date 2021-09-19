from django.contrib.auth import admin
from django.contrib.auth.models import User
from django.db import models

class CustomerPreferenceAnswer(models.Model):
    customer = models.ForeignKey("Customer.Customer", on_delete=models.CASCADE)
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

    question = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DROP_DOWN)

    def serialize(self):
        return {
            'id': self.id,
            'question': self.question,
            'description': self.description,
            'type': self.type,
            'options': [ans.serialize() for ans in self.preferenceanswer_set.all()]
        }


class PreferenceAnswer(models.Model):
    preference_question = models.ForeignKey("PreferenceQuestion", on_delete=models.CASCADE)
    answer = models.CharField(max_length=10)

    class Meta:
        unique_together = ['preference_question', 'answer']

    def serialize(self):
        return {
            'id': self.id,
            'answer': self.answer
        }
