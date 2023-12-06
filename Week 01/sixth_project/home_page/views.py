from django.shortcuts import render

# Create your views here.
def common(request):
    return render(request,'main.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def course(request):
    return render(request,'course.html', {'author': 'Karim'})