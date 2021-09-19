from django.contrib.auth.models import User
# from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import CustomerPreferenceAnswer, PreferenceQuestion, PreferenceAnswer


class PreferenceQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreferenceQuestion
        fields = "__all__"

class PreferenceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreferenceAnswer
        fields = "__all__"