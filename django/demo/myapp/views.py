from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('welcome to login page')
def contact(request):
    return HttpResponse('welcome to contact page')
def srvice(request):
    return HttpResponse('welcome to service page')
