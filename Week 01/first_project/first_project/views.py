from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Django,This is my Home page")

def about(request):
    return HttpResponse('This is my About page')