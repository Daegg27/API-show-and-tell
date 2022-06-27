from django.urls import path
from . import views

app_name = "nba_app"
urlpatterns = [
    path("", views.index, name="home"),
    path("teams/", views.find_teams, name="browse"),
    path("conference/<str:team>/", views.found_team, name="complete")
    # path("help", views.test)
]