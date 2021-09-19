from django.urls import path

# from .views import ListCreateCustomerPreferenceAnswer
import RideFeedback.views


app_name = "RideFeedback"

urlpatterns = [
    path('submit_feedback', RideFeedback.views.submit_feedback, name='submit_feedback'),
    path('get_voting_options', RideFeedback.views.get_voting_options, name='get_voting_options'),
]