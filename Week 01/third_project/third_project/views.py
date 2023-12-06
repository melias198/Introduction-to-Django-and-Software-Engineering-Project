# from django.views.generic import TemplateView

# class Home(TemplateView):
#     template_name = 'index.html'

from django.shortcuts import render

def home(request):
    return render(request,'index.html')