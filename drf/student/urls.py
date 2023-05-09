from django.urls import path
from .views import StudentCreateApi,StudentApi,StudentUpdateApi,StudentDeleteApi


urlpatterns = [

    path('apistu', StudentApi.as_view()),
    path('apistu/create', StudentCreateApi.as_view()),
    path('apistu/<int:pk>', StudentUpdateApi.as_view()),
    path('apistu/delete/<int:pk>',StudentDeleteApi.as_view()),


]




