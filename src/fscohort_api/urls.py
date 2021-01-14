from django.urls import path
from .views import home_api, student_list_api, student_create_api

urlpatterns = [
    path("home-api/", home_api),
    path("list-api/", student_list_api),
    path("create-api/", student_create_api),
]
