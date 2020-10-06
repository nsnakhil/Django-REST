from django.urls import path
from frontend_todo import views

urlpatterns=[
    path('', views.list, name = "list"),
]