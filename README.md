<h1 align="center">Making of Django REST Project</h1>

1. Use the  [Django CRUD Project](https://github.com/SemihDurmus/Django_Forms_CRUD) for initial files and settings.
2. Create another app "fscohort_api" + add to settings.py INSTALLED_APPS + create fscohort_api > urls.py file + include  fscohort_api to main urls.py
3. Import JsonResponse from django.http in fscohort_api > views
4. Create a func named home_api in views and add a dictionary structured static data in. We will soon change it to dynamic.
5. Import home_api to urls and define a path
6. Run server + check the path http://localhost:8000/api/home-api/ see the json file
7. Open "Postman" use the same url + GET. Make sure you see the same json file