from django.urls import path
# student_list_api, student_create_api
from .views import home_api
# from .views import student_list_create_api, student_get_update_delete #FUNCTION BASED VIEWS
# from .views import StudentList, StudentGetUpdateDelete  # CLASS BASED VIEWS
from .views import StudentList, StudentGetUpdateDelete  # GENERIC VIEWS


urlpatterns = [
    path("home-api/", home_api),
    # path("list-api/", student_list_api),
    # path("create-api/", student_create_api),
    # path("list-create-api/", student_list_create_api), #FUNCTION BASED VIEW'S PATH
    # path("<int:id>/", student_get_update_delete), #FUNCTION BASED VIEW'S PATH
    # path("list-create-api/", StudentList.as_view()),  # CLASS BASED VIEW'S PATH
    # path("<int:id>/", StudentGetUpdateDelete.as_view()),# CLASS BASED VIEW'S PATH
    path("list-create-api/", StudentList.as_view()),  # GENERIC VIEW'S PATH
    path("<int:id>/", StudentGetUpdateDelete.as_view(),
         name="detail"),  # GENERIC VIEW'S PATH

]
