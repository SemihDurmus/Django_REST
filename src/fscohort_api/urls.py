from django.urls import path
# student_list_api, student_create_api
from .views import home_api, student_list_create_api, student_get_update_delete

urlpatterns = [
    path("home-api/", home_api),
    # path("list-api/", student_list_api),
    # path("create-api/", student_create_api),
    path("list-create-api/", student_list_create_api),
    path("<int:id>/", student_get_update_delete),
]
