
from django.urls import path, include

# from .views import ListCreateCustomerPreferenceAnswer
import Preference.views

app_name = "Preference"

urlpatterns = [
    path('customer_preference_answer/', ListCreateCustomerPreferenceAnswer.as_view(), name='customer_preference_answer'),
    # path('<int:id>', GetCustomerPreference.as_view(), name='retreive_preference'),
    # path('user_preference/', include('Preference.urls', "Preference")),
    path(r'^preference_questions/$', Preference.views.get_all_questions_with_options, name='preference_questions'),
]