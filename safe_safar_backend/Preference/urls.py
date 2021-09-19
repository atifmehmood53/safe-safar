
from django.urls import path, include

import Preference.views
# from .views import ListCreateCustomerPreference, GetCustomerPreference

app_name = "Preference"

urlpatterns = [
    # path('', ListCreateCustomerPreference.as_view(), name='create_preference'),
    # path('<int:id>', GetCustomerPreference.as_view(), name='retreive_preference'),
    # path('user_preference/', include('Preference.urls', "Preference")),
    # path('preference_questions/', include('Preference.urls', "Preference.views.get_all_questions_with_options")),
    path('preference_questions', Preference.views.get_all_questions_with_options, name='preference_questions'),
    path('submit_preferences', Preference.views.submit_customer_selected_preferences, name='submit_preferences'),
    path('retrieve_preferences', Preference.views.get_customer_selected_preferences, name='retrieve_preferences'),
]