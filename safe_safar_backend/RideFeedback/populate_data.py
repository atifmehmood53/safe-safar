
import Customer.models
import RideFeedback.models

Customer = Customer.models.Customer
Seat = RideFeedback.models.Seat
Ride = RideFeedback.models.Ride
PalFeedback = RideFeedback.models.PalFeedback
Booking = RideFeedback.models.Booking


def populate():
    ride = Ride.objects.create(name='van1')
    seat_1a = Seat.objects.create(seat_number='1a', ride=ride)
    seat_1b = Seat.objects.create(seat_number='1b', ride=ride)
    seat_1c = Seat.objects.create(seat_number='1c', ride=ride)
    seat_2a = Seat.objects.create(seat_number='2a', ride=ride)
    seat_2b = Seat.objects.create(seat_number='2b', ride=ride)
    seat_2c = Seat.objects.create(seat_number='2c', ride=ride)

    customer_1 = Customer.objects.create(username='c1', community_score=1.0)
    customer_2 = Customer.objects.create(username='c2', community_score=1.0)
    customer_3 = Customer.objects.create(username='c3', community_score=1.0)
    customer_4 = Customer.objects.create(username='c4', community_score=1.0)
    customer_5 = Customer.objects.create(username='c5', community_score=1.0)
    customer_6 = Customer.objects.create(username='c6', community_score=1.0)

    booking_1 = Booking.objects.create(customer=customer_1, seat=seat_1a)
    booking_2 = Booking.objects.create(customer=customer_2, seat=seat_1b)
    booking_3 = Booking.objects.create(customer=customer_3, seat=seat_1c)
    booking_4 = Booking.objects.create(customer=customer_4, seat=seat_2a)
    booking_5 = Booking.objects.create(customer=customer_5, seat=seat_2b)
    booking_6 = Booking.objects.create(customer=customer_6, seat=seat_2c)

    booking_1.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    booking_3.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    booking_4.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    booking_5.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    booking_6.provide_feedback_to_booking(booking_2, PalFeedback.BLACKLIST)
    booking_1.provide_feedback_to_booking(booking_3, PalFeedback.UP)
    booking_4.provide_feedback_to_booking(booking_3, PalFeedback.NEUTRAL)
