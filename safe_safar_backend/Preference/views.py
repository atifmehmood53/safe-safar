from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
# from rest_framework import generics
from django.views.decorators.http import require_POST
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from .models import CustomerPreferenceAnswer, PreferenceQuestion
# from .serializers import UserPreferenceSerializer

# class ListCreateCustomerPreference(generics.CreateAPIView):
#     queryset = CustomerPreferenceAnswer.objects.all()
#     serializer_class = UserPreferenceSerializer
#
# class GetCustomerPreference(generics.RetrieveAPIView):
#     queryset = CustomerPreferenceAnswer.objects.all()
#     serializer_class = UserPreferenceSerializer
#     lookup_field = "id"


def get_all_questions_with_options(request):
    all_questions = [q.serialize() for q in PreferenceQuestion.objects.all()]
    return JsonResponse(all_questions, safe=False)


@api_view(['POST'])
@parser_classes([JSONParser])
def submit_customer_selected_preferences(request):
    customer_id = request.data['customer_id']
    answer_ids = request.data['answers']
    cpa, _ = CustomerPreferenceAnswer.objects.get_or_create(customer_id=customer_id)
    cpa.preference_answers.add(*answer_ids)
    return JsonResponse({'success': True})


def get_customer_selected_preferences(request):
    customer_id = request.GET['customer_id']
    answers = list(
        CustomerPreferenceAnswer.objects.filter(customer_id=customer_id).values_list('preference_answers', flat=True))
    return JsonResponse({'answers': answers})
