from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from .models import CustomerPreferenceAnswer, PreferenceQuestion
from .serializers import UserPreferenceSerializer

class ListCreateCustomerPreference(generics.CreateAPIView):
    queryset = CustomerPreferenceAnswer.objects.all()
    serializer_class = UserPreferenceSerializer

class GetCustomerPreference(generics.RetrieveAPIView):
    queryset = CustomerPreferenceAnswer.objects.all()
    serializer_class = UserPreferenceSerializer
    lookup_field = "id"


def get_all_questions_with_options(request):
    all_questions = [q.serialize() for q in PreferenceQuestion.objects.all()]
    return JsonResponse(all_questions, safe=False)
