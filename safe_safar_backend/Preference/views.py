from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from .models import CustomerPreferenceAnswer, PreferenceQuestion, PreferenceAnswer
from .serializers import CustomerPreferenceAnswerSerializer, PreferenceQuestionSerializer, PreferenceAnswerSerializer


class ListCreateCustomerPreferenceAnswer(generics.ListCreateAPIView):
    queryset = CustomerPreferenceAnswer.objects.all()
    serializer_class = CustomerPreferenceAnswerSerializer

class GetCustomerPreferenceAnswer(generics.RetrieveAPIView):
    queryset = CustomerPreferenceAnswer.objects.all()
    serializer_class = CustomerPreferenceAnswerSerializer
    lookup_field = "id"

class ListCreatePreferenceQuestion(generics.ListCreateAPIView):
    queryset = PreferenceQuestion.objects.all()
    serializer_class = PreferenceQuestionSerializer

class GetPreferenceQuestion(generics.RetrieveAPIView):
    queryset = PreferenceQuestion.objects.all()
    serializer_class = PreferenceQuestionSerializer
    lookup_field = "id"

class ListCreatePreferenceAnswer(generics.ListCreateAPIView):
    queryset = PreferenceAnswer.objects.all()
    serializer_class = PreferenceAnswerSerializer

class GetPreferenceAnswer(generics.RetrieveAPIView):
    queryset = PreferenceAnswer.objects.all()
    serializer_class = PreferenceAnswerSerializer
    lookup_field = "id"


def get_all_questions_with_options(request):
    all_questions = [q.serialize() for q in PreferenceQuestion.objects.all()]
    return JsonResponse(all_questions, safe=False)
