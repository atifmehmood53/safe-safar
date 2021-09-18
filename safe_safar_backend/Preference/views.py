from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from .models import CustomerPreferenceAnswer
from .serializers import UserPreferenceSerializer

class ListCreateCustomerPreference(generics.CreateAPIView):
    queryset = CustomerPreferenceAnswer.objects.all()
    serializer_class = UserPreferenceSerializer

class GetCustomerPreference(generics.RetrieveAPIView):
    queryset = CustomerPreferenceAnswer.objects.all()
    serializer_class = UserPreferenceSerializer
    lookup_field = "id"