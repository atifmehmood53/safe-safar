
from django.urls import path, include

from .views import ListCreateCustomerPreference

app_name = "Preference"

urlpatterns = [
    path('', ListCreateCustomerPreference.as_view(), name='create_preference'),
    # path('user_preference/', include('Preference.urls', "Preference")),
]