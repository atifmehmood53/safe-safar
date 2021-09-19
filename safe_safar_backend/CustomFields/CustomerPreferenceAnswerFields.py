from rest_framework import serializers

import Preference as test
from Customer.models import Customer
from Preference.models import PreferenceAnswer

class CustomerField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(CustomerField, self).to_representation(value)
        try:
            item = Customer.objects.get(pk=pk)
            from safe_safar_backend.Customer.serializers import CustomerSerializer
            print("sss")
            serializer = CustomerSerializer(item)
            return serializer.data
        except Customer.DoesNotExist:

            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

class PreferenceAnswerField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(PreferenceAnswerField, self).to_representation(value)
        try:
            item = PreferenceAnswer.objects.get(pk=pk)
            from Preference.serializers import PreferenceAnswerSerializer
            # from PreferenceAnswer.serializers import TripSerializer
            print("sss")
            serializer = PreferenceAnswerSerializer(item)
            return serializer.data
        except PreferenceAnswer.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}