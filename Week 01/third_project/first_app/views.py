from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,'./first_app/index.html', context={'name': 'Mohammad Elias' , 'age': 20, 'marks': 30, 'courses':
        [
            {
                'id': 101,
                'course': 'C',
                'teacher': 'Farhan Firoz'
            },
            {
                'id': 102,
                'course': 'C++',
                'teacher': 'Rahat Khan Pathan'
            },
            {
                'id': 103,
                'course': 'Python',
                'teacher': 'Jhankar Mahbub'
            }
        ],
        'blog': 'there are some mandatory people who had need at the moment',
        'lst': [30,20,50]})

