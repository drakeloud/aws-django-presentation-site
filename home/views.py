from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, Jason! You’re at the home index and this is a test!")
