from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse('''
                        This is Courses Page.
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/second_app/feedback/'>Feedback</a>
                        ''')

def feedback(request):
    return HttpResponse('''
                        This is Feedback Page.
                        <a href = '/first_app/contact/'>Contact</a>
                        <a href = '/first_app/about/'>About</a>
                        <a href = '/second_app/courses/'>Courses</a>
                        ''')