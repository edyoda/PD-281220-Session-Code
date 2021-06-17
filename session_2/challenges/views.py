from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is working !!")


def index2(request):
    return HttpResponse("This is working Feb!!")
