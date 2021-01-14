from django.shortcuts import render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt


def home_api(request):
    data = {
        "name": "henry",
        "address": "clarusway.com",
        "skills": ["python", "django"]
    }
    return JsonResponse(data)


# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()

#         student_list = []
#         for student in students:
#             student_list.append({
#                 'first_name': student.first_name,
#                 'last_name': student.last_name,
#                 'number': student.number
#             })

#     data = {
#         "students": student_list,
#         "count": student_count
#     }
#     return JsonResponse(data)

def student_list_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        student_count = Student.objects.count()
        student_data = serialize("python", students)

        data = {
            "students": student_data,
            "count": student_count
        }

    return JsonResponse(data)


@csrf_exempt
def student_create_api(request):
    if request.method == "POST":
        post_body = json.loads(request.body)
        print(type(post_body))  # <class 'dict'>
        name = post_body.get("first_name")
        last_name = post_body.get("last_name")
        number = post_body.get("number")

        student_data = {
            "first_name": name,
            "last_name": last_name,
            "number": number
        }

        student_obj = Student.objects.create(**student_data)
        data = {
            "message": f"Student {student_obj.first_name} created successfully"
        }
        return JsonResponse(data, status=201)
