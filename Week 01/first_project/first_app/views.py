from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello from home page inside app')

def about(request):
    return HttpResponse('Hello from about page inside app')