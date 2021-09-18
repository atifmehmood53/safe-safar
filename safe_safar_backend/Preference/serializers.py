from django.contrib.auth.models import User
from rest_framework import serializers

# from safe_safar_backend.Preference.models import UserPreference


class UserPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        depth = 2