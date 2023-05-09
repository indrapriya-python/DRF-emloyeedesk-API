

from django.urls import path
from .views import EmployeeCreateApi,EmployeeApi,EmployeeUpdateApi,EmployeeDeleteApi


urlpatterns = [

    path('api', EmployeeApi.as_view()),
    path('api/create', EmployeeCreateApi.as_view()),
    path('api/<int:pk>', EmployeeUpdateApi.as_view()),
    path('api/delete/<int:pk>', EmployeeDeleteApi.as_view()),

]
