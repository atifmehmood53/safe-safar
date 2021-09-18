import Preference.models

import RideFeedback.models

Customer = Preference.models.Customer
Seat = RideFeedback.models.Seat
Ride = RideFeedback.models.Ride
PalFeedback = RideFeedback.models.PalFeedback


def populate():
    ride = Ride.objects.create(name='van1')
    seat_1a = Seat.objects.create(seat_number='1a', ride=ride)
    seat_1b = Seat.objects.create(seat_number='1b', ride=ride)
    seat_1c = Seat.objects.create(seat_number='1c', ride=ride)

    customer_1 = Customer.objects.create(username='c1', community_score=1.0)
    customer_2 = Customer.objects.create(username='c2', community_score=1.0)
    customer_3 = Customer.objects.create(username='c3', community_score=1.0)

    booking_1 = RideFeedback.models.Booking.objects.create(customer=customer_1, seat=seat_1a)
    booking_2 = RideFeedback.models.Booking.objects.create(customer=customer_2, seat=seat_1b)
    booking_3 = RideFeedback.models.Booking.objects.create(customer=customer_3, seat=seat_1c)

    pal_feedback_1 = PalFeedback.objects.create(booking=booking_1, pal_booking=booking_2, vote=PalFeedback.DOWN)
    pal_feedback_2 = PalFeedback.objects.create(booking=booking_2, pal_booking=booking_1, vote=PalFeedback.DOWN)
    pal_feedback_3 = PalFeedback.objects.create(booking=booking_2, pal_booking=booking_3, vote=PalFeedback.UP)
    pal_feedback_4 = PalFeedback.objects.create(booking=booking_3, pal_booking=booking_2, vote=PalFeedback.NEUTRAL)
