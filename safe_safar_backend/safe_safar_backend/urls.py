
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user_feedback/', include('RideFeedback.urls', "RideFeedback")),
    path('user_preference/', include('Preference.urls', "Preference")),
]
