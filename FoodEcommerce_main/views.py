from django.shortcuts import render
from django.http import HttpResponse

def home(requeset):
    return HttpResponse('Hello World!')