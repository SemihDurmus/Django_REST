from django.urls import path
from .views import home_api

urlpatterns = [
    path("home-api/", home_api)
]
