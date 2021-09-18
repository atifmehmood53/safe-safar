from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class User(User):
    community_score = models.FloatField()


class UserPreferenceAnswer(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    preference_answers = models.ManyToManyField("PreferenceAnswer")


class PreferenceQuestion(models.Model):
    question = models.CharField(max_length=20)
    description = models.CharField(max_length=50)


class PreferenceAnswer(models.Model):
    preference_question = models.ForeignKey("PreferenceQuestion", on_delete=models.CASCADE)
    answer = models.CharField(max_length=10)

    class Meta:
        unique_together = ['preference_question', 'answer']