from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests as HTTP_Client

# Create your views here.
def index(request):
    
    return HttpResponse("<h1>Are you in need of some NCAA knowledge!?!?!?</h1>")

def find_teams(request):
    url = "https://api.collegefootballdata.com/teams?conference=B1G"

    headers = {
        "Authorization": "Bearer /NBzI8ALvb7kB+AtbqVv6P4Fkkv/J4jv0hcgE95Tc7XZ0RxyB7F8EI67LPORge3H"
    }

    response = HTTP_Client.get(url, headers=headers)
    responseJSON = response.json()
    
    print(responseJSON)
    return HttpResponse("<h1>Nice work!</h1>")
