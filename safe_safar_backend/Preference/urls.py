
from django.urls import path, include

from .views import ListCreateCustomerPreference, GetCustomerPreference

app_name = "Preference"

urlpatterns = [
    path('', ListCreateCustomerPreference.as_view(), name='create_preference'),
    path('<int:id>', GetCustomerPreference.as_view(), name='retreive_preference'),
    # path('user_preference/', include('Preference.urls', "Preference")),
]