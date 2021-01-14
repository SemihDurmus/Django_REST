<h1 align="center">Making of Django REST Project</h1>

1. Use the  [Django CRUD Project](https://github.com/SemihDurmus/Django_Forms_CRUD) for initial files and settings.
2. Create another app "fscohort_api" + add to settings.py INSTALLED_APPS + create fscohort_api > urls.py file + include  fscohort_api to main urls.py
3. Import JsonResponse from django.http in fscohort_api > views
4. Create a func named home_api in views and add a dictionary structured static data in. We will soon change it to dynamic.
5. Import home_api to urls and define a path
6. Run server + check the path http://localhost:8000/api/home-api/ see the json file
7. Open "Postman" use the same url + GET. Make sure you see the same json file
8. Import student from models to fscohort_api > views. Two methods for displaying data in database (as objecs) in json form:
 * 
```python
def student_list_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        student_count = Student.objects.count()

        student_list = []
        for student in students:
            student_list.append({
                'first_name': student.first_name,
                'last_name': student.last_name,
                'number': student.number
            })

    data = {
        "students": student_list,
        "count": student_count
    }
    return JsonResponse(data)
```
 * Use serializer. `from django.views.decorators.csrf import csrf_exempt
`
```python
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
```
9. Now we want to do the opposite. We want the transform the json data sent from backend to dictionary form in order to save to database. `import json`. This is for converting json to dict.
```python
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
```
Since we do not have a frontend at the moment, we use POSTMAN to send json data. (POST-Body-raw). 
```json
{
    "first_name": "Eric",
    "last_name": "Emerson",
    "number": 5
}
```
To get rid of csrf error add `from django.views.decorators.csrf import csrf_exempt` and also add `@csrf_exempt` before function. We could have not used name, last_name and number variables and student_data as well + `student_obj = Student.objects.create(**post_data)` instead, because the data in body is exactly the same as we have in db. But otherwise we have to define the data structure.

10. Install rest_framework `python3 -m pip install djangorestframework` and add `rest_framework` to INSTALLED_APPS in settings.py

11. Django REST helps us automatically serialize data, so that we do not have to write long line of codes.

12. Create serializers.py under fscohort_api, import Student model and create a class as below
```python
from rest_framework import serializers
from fscohort.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number"]
```
Note that this is very similar to a form.

13. Now go to views and comment out all functions except home_api. Import the following
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status
```
14. Add this function:
```python
@api_view(["GET", "POST"])
def student_list_create_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # many=True because we get many objects
        return Response(serializer.data) #.data is default
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student created successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
15. Remove the commented out imported functions in urls and import `student_list_create_api` + add the path
16. Check if you see djangos fantasic page on `http://localhost:8000/api/list-create-api/`
17. Check also from POSTMAN with the same url both with GET and POST. If you get "Unsupported media type" error with POST, go to Headers and add `Content-Type` under KEY column and `application/json` under VALUE column. Then try again.