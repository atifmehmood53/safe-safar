
import Customer.models
import RideFeedback.models

Customer = Customer.models.Customer
Seat = RideFeedback.models.Seat
Ride = RideFeedback.models.Ride
PalFeedback = RideFeedback.models.PalFeedback
Booking = RideFeedback.models.Booking


def populateBooking():
    ride = Ride.objects.create(name='van1')
    seat_1 = Seat.objects.create(seat_number='1', ride=ride)
    seat_2 = Seat.objects.create(seat_number='2', ride=ride)
    seat_3 = Seat.objects.create(seat_number='3', ride=ride)
    seat_4 = Seat.objects.create(seat_number='4', ride=ride)
    seat_5 = Seat.objects.create(seat_number='5', ride=ride)
    seat_6 = Seat.objects.create(seat_number='6', ride=ride)
    seat_7 = Seat.objects.create(seat_number='7', ride=ride)
    seat_8 = Seat.objects.create(seat_number='8', ride=ride)
    seat_9 = Seat.objects.create(seat_number='9', ride=ride)
    seat_10 = Seat.objects.create(seat_number='10', ride=ride)
    seat_11 = Seat.objects.create(seat_number='11', ride=ride)
    seat_12 = Seat.objects.create(seat_number='12', ride=ride)

    customer_1 = Customer.objects.create(username='c1', community_score=1.0)
    customer_2 = Customer.objects.create(username='c2', community_score=1.0)
    customer_3 = Customer.objects.create(username='c3', community_score=1.0)
    customer_4 = Customer.objects.create(username='c4', community_score=1.0)
    customer_5 = Customer.objects.create(username='c5', community_score=1.0)
    customer_6 = Customer.objects.create(username='c6', community_score=1.0)
    customer_7 = Customer.objects.create(username='c7', community_score=1.0)
    customer_8 = Customer.objects.create(username='c8', community_score=1.0)
    customer_9 = Customer.objects.create(username='c9', community_score=1.0)
    customer_10 = Customer.objects.create(username='c10', community_score=1.0)
    customer_11 = Customer.objects.create(username='c11', community_score=1.0)
    customer_12 = Customer.objects.create(username='c12', community_score=1.0)

    booking_1 = Booking.objects.create(customer=customer_1, seat=seat_1)
    booking_2 = Booking.objects.create(customer=customer_2, seat=seat_2)
    booking_3 = Booking.objects.create(customer=customer_3, seat=seat_3)
    booking_4 = Booking.objects.create(customer=customer_4, seat=seat_4)
    booking_5 = Booking.objects.create(customer=customer_5, seat=seat_5)
    booking_6 = Booking.objects.create(customer=customer_6, seat=seat_6)
    booking_7 = Booking.objects.create(customer=customer_7, seat=seat_7)
    booking_8 = Booking.objects.create(customer=customer_8, seat=seat_8)
    booking_9 = Booking.objects.create(customer=customer_9, seat=seat_9)
    booking_10 = Booking.objects.create(customer=customer_10, seat=seat_10)
    booking_11 = Booking.objects.create(customer=customer_11, seat=seat_11)
    booking_12 = Booking.objects.create(customer=customer_12, seat=seat_12)

    # booking_1.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    # booking_3.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    # booking_4.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    # booking_5.provide_feedback_to_booking(booking_2, PalFeedback.DOWN)
    # booking_6.provide_feedback_to_booking(booking_2, PalFeedback.BLACKLIST)
    # booking_1.provide_feedback_to_booking(booking_3, PalFeedback.UP)
    # booking_4.provide_feedback_to_booking(booking_3, PalFeedback.NEUTRAL)
