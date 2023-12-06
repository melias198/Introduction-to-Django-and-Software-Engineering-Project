from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'./second_app/index.html', context={ 'courses':
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
        ]})