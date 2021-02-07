# my_app/urls.py
from django.urls import path

from my_app import views

urlpatterns = [
    path("info/", views.school_json),
]


