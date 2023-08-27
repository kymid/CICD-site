from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request): #HttpRequest
    return HttpResponse('OwnProject')