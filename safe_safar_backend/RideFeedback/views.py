from django.http import JsonResponse

# Create your views here.
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from .models import Booking, PalFeedback


@api_view(['POST'])
@parser_classes([JSONParser])
def submit_feedback(request):
    from_booking = request.data['booking_id']
    to_booking = request.data['pal_booking_id']
    vote = request.data['vote']

    booking = Booking.objects.get(id=from_booking)
    pal_booking = Booking.objects.get(id=to_booking)

    booking.provide_feedback_to_booking(pal_booking, vote)

    return JsonResponse({'success': True})


def get_voting_options(request):
    return JsonResponse({label: weight for (weight, label) in PalFeedback.VOTE_CHOICES})
