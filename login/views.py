from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("This is the login page. " + request.META['REQUEST_METHOD'])

@csrf_exempt
def new_login(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body['username']
    password = body['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"username": username, "password": password, "loggedIn": "True"})
        # Redirect to a success page.
    else:
       return JsonResponse({"username": username, "password": password, "loggedIn": "False"})
        #Return an 'invalid login' error message.