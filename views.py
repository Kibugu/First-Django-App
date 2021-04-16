from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("My name is James G Kibugu am currently Age  32 years my  Profession is Data Scientist/analyst/Developer Currently location: Nairobi Kenya ")
