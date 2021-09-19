
from django.urls import path, include

# from .views import ListCreateCustomerPreferenceAnswer
import Preference.views

# from safe_safar_backend.Preference.views import ListCreateCustomerPreferenceAnswer
from Preference.views import ListCreateCustomerPreferenceAnswer

app_name = "Preference"

urlpatterns = [
    # path('customer_preference_answer/', ListCreateCustomerPreferenceAnswer.as_view(), name='customer_preference_answer'),
    # path('<int:id>', GetCustomerPreference.as_view(), name='retreive_preference'),
    # path('user_preference/', include('Preference.urls', "Preference")),
    # path('preference_questions/', include('Preference.urls', "Preference.views.get_all_questions_with_options")),
    path('preference_questions', Preference.views.get_all_questions_with_options, name='preference_questions')
    # path(preference_questions', Preference.views.get_all_questions_with_options, name='preference_questions'),
]