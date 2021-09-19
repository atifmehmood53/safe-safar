from rest_framework import serializers

from safe_safar_backend.Customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"