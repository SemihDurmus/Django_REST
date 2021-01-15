from django.urls import path
# student_list_api, student_create_api
from .views import home_api
# from .views import student_list_create_api, student_get_update_delete #FUNCTION BASED VIEWS
# from .views import StudentList, StudentGetUpdateDelete  # CLASS BASED VIEWS
# from .views import StudentList, StudentGetUpdateDelete  # GENERIC VIEWS
from .views import Student  # MIXIN VIEWS


urlpatterns = [
    path("home-api/", home_api),
    # -----------REGULAR----------------
    # path("list-api/", student_list_api),
    # path("create-api/", student_create_api),
    # -----------FUNCTION BASED ----------------
    # path("list-create-api/", student_list_create_api), #FUNCTION BASED VIEW'S PATH
    # path("<int:id>/", student_get_update_delete), #FUNCTION BASED VIEW'S PATH
    # -----------CLASS BASED ----------------
    # path("list-create-api/", StudentList.as_view()),  # CLASS BASED VIEW'S PATH
    # path("<int:id>/", StudentGetUpdateDelete.as_view()),# CLASS BASED VIEW'S PATH
    # -----------GENERIC ----------------
    # path("list-create-api/", StudentList.as_view()),  # GENERIC VIEW'S PATH
    # path("<int:id>/", StudentGetUpdateDelete.as_view(),name="detail"),  # GENERIC VIEW'S PATH
    # -----------MIXIN ----------------
    path("<int:id>/", Student.as_view(), name="detail"),  # GENERIC VIEW'S PATH

]
