from django.urls import path
from . import views

app_name = "nba_app"
urlpatterns = [
    path("", views.index, name="home"),
    path("conferences/", views.find_teams, name="browse"),
    path("conference/<str:conference>/", views.select_team, name="complete"),
    path("conference/<str:conference>/<str:team>", views.view_team, name="destination")
    # path("conference/<str:team>/<str:school>/", views.found_team, name="complete")
]