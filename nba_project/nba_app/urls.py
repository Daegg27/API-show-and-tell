from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("teams/", views.find_teams)
]