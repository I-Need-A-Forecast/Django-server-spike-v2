from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Person
import json


# Create your views here.




def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    
    p = Person.objects.raw('SELECT * FROM wx.db_tests_person')
    
    x = {
        "Salutations": [
        ]
    }
    for person in p:
        x["Salutations"].append({
            'FirstName': person.first_name,
            'Lastname': person.last_name
        })

    return JsonResponse(x)

    #return JsonResponse({"Greeting": {'Firstname': p[0].first_name, 'Lastname': p[0].last_name}})
    #return JsonResponse({"Greeting": p[0].first_name})

def index2(request):

    r = Person.objects.raw('Select temp_f FROM wx.current_observation WHERE station_id = "kmsp"')

    t = {
        "Hello": [
        ]
    }
    for tester in r:
        t["Hello"].append({
            "temperature": tester.temp_f,
        })

    return JsonResponse(t)