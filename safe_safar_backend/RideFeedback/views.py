from django.http import JsonResponse

# Create your views here.
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from .models import Booking, PalFeedback


@api_view(['POST'])
@parser_classes([JSONParser])
def submit_feedback(request):
    PalFeedback.objects.all().delete()
    customer_id = request.data['customer_id']
    seat_votes = request.data.get_list('seat_votes')
    customer_booking = Booking.objects.get(customer_id=customer_id)
    for seat_vote in seat_votes:
        pal_booking = Booking.objects.get(seat__seat_number=seat_vote['seat'])
        vote = seat_vote['vote']
        customer_booking.provide_feedback_to_booking(pal_booking, vote)

    return JsonResponse({'success': True})


def get_voting_options(request):
    return JsonResponse({label: weight for (weight, label) in PalFeedback.VOTE_CHOICES})
