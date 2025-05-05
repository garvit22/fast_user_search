from django.urls import path
from .views import check_username

urlpatterns = [
    path('check/', check_username),
]
