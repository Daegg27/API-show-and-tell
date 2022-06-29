from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests as HTTP_Client


# ['ACC', 'B12', 'B1G', 'SEC', 'PAC', 'CUSA', 'MAC', 'MWC', 'Ind']
def condense_conference(word):
    if word == "Big 10":
        return 'B1G'
    elif word == "FBS Independents":
        return 'Ind'
    elif word == "Mountain West":
        return 'MWC'
    elif word == "Mid-American":
        return "MAC"
    elif word == "Conference USA":
        return "CUSA"
    elif word == "Pac-12":
        return "PAC"
    elif word == "SEC":
        return "SEC"
    elif word == "Big 12":
        return "B12"
    elif word == "ACC":
        return "ACC"
    else:
        return "Confusion"
    

# Create your views here.
def index(request):
    
    return HttpResponse("<h1>Are you in need of some NCAA knowledge!?!?!?</h1>")

def find_teams(request):
    url = "https://api.collegefootballdata.com/conferences"
    # url = "https://api.collegefootballdata.com/teams?conference=B1G"

    headers = {
        "Authorization": "Bearer /NBzI8ALvb7kB+AtbqVv6P4Fkkv/J4jv0hcgE95Tc7XZ0RxyB7F8EI67LPORge3H"
    }

    # placeholder query string

    all_conferences = []
    response = HTTP_Client.get(url, headers=headers)
    responseJSON = response.json()

    # Creates a list of all major D-1 conferences
    for x in range(0, 9):
        all_conferences.append(responseJSON[x]['abbreviation'])
    
    
    
    print(all_conferences)
    # print(responseJSON[3]['abbreviation'])
    # url = f"https://api.collegefootballdata.com/teams/?conference={all_conferences[1]}"
    # response = HTTP_Client.get(url, headers=headers)
    # responseJSON = response.json()
    # print(responseJSON)

    my_data = {
        "all_conferences": all_conferences
    }

    return render(request, "index.html", my_data)

def select_team(request, conference):
    url = f"https://api.collegefootballdata.com/teams?conference={conference}"

    headers = {
        "Authorization": "Bearer /NBzI8ALvb7kB+AtbqVv6P4Fkkv/J4jv0hcgE95Tc7XZ0RxyB7F8EI67LPORge3H"
    }
    
    list_of_teams = []
    response = HTTP_Client.get(url, headers=headers)
    responseJSON = response.json()

    for data in responseJSON:
        list_of_teams.append(data['school'])
    conference = condense_conference(responseJSON[0]['conference'])
    print(conference)
    # print(list_of_teams)
    # print(responseJSON[0])

    my_data = {
        'list_of_teams': list_of_teams,
        "conference":conference
    }

    return render(request, 'team_search.html', my_data)

def view_team(request, conference, team):
    pass



    
