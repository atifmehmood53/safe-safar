from django.contrib.auth.models import User
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import CustomerPreferenceAnswer, PreferenceQuestion, PreferenceAnswer

class CustomerPreferenceAnswerSerializer(WritableNestedModelSerializer):
    from CustomFields.CustomerPreferenceAnswerFields import CustomerField, PreferenceAnswerField
    from Customer.models import Customer

    customer = CustomerField(read_only=False,queryset=Customer.objects.all())
    preference_answers = PreferenceAnswerField(read_only=False,queryset=PreferenceAnswer.objects.all())
    class Meta:
        model = CustomerPreferenceAnswer
        fields = "__all__"
        depth = 2

class PreferenceQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreferenceQuestion
        fields = "__all__"

class PreferenceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreferenceAnswer
        fields = "__all__"