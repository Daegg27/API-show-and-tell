from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests as HTTP_Client

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

def found_team(request, team):
    url = f"https://api.collegefootballdata.com/teams?conference={team}"

    headers = {
        "Authorization": "Bearer /NBzI8ALvb7kB+AtbqVv6P4Fkkv/J4jv0hcgE95Tc7XZ0RxyB7F8EI67LPORge3H"
    }
    getElementById("school-name")
    # hi =  request.POST['school-name']
    # print(hi)
    response = HTTP_Client.get(url, headers=headers)
    responseJSON = response.json()

    # print(responseJSON)

    return HttpResponse("<h1>Button has worked</h1>")

def test(request):
    url = "https://api.collegefootballdata.com/teams"

    headers = {
        "Authorization": "Bearer /NBzI8ALvb7kB+AtbqVv6P4Fkkv/J4jv0hcgE95Tc7XZ0RxyB7F8EI67LPORge3H"
    }

    response = HTTP_Client.get(url, headers=headers)
    responseJSON = response.json()
    print(responseJSON[42]['location'])

    return HttpResponse("<h1>Nice work!</h1>")

    
