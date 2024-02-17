from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import TaskModel

# Create your views here.
def home(request):
    tasks = TaskModel.objects.all()
    return render(request,'home.html',{'tasks':tasks})


def store_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    
    return render(request,'store_task.html',{'form':form})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request,'show_tasks.html',{'tasks':tasks})


def delete_task(request,id):
    TaskModel.objects.get(pk = id).delete()
    return redirect('show_tasks')


def edit_task(request,id):
    task = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
        
    return render(request,'edit_task.html',{'form':form})


def complete_task(request,id):
    tasks = TaskModel.objects.all()
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    
    return render(request,'complited_task.html',{'tasks':tasks})


def view_complete(request):
    tasks = TaskModel.objects.all()
    return render(request,'view_complete.html',{'tasks':tasks})
    
        
    
    