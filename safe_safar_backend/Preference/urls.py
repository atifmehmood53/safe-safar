
from django.urls import path, include

from .views import ListCreateCustomerPreferenceAnswer

app_name = "Preference"

urlpatterns = [
    path('customer_preference_answer/', ListCreateCustomerPreferenceAnswer.as_view(), name='customer_preference_answer'),
    # path('<int:id>', GetCustomerPreference.as_view(), name='retreive_preference'),
    # path('user_preference/', include('Preference.urls', "Preference")),
]