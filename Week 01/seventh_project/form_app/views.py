from django.shortcuts import render
from . forms import ContactForm,StudentData,PasswordMatch
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./form_app/upload/'+ file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'home.html', {'form':form})
    else:
        form = StudentData()
    return render(request,'home.html',{'form':form})



def about(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        password = request.POST.get('user_pass')
        return render(request,'about.html',{'name':name,'email':email,'password':password})
    return render(request,'about.html')


def rating(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        movie_name = request.POST.get('movie_name')
        rating = request.POST.get('rating')
        return render(request,'rating.html',{'name':name, 'email':email, 'movie_name':movie_name, 'rating':rating})
    return render(request,'rating.html')


def django_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./form_app/upload/'+ file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'form.html',{'form':form})
    else:
        form = ContactForm()
    return render(request,'form.html',{'form':form})


def sign_up(request):
    if request.method == 'POST':
        form = PasswordMatch(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'sign_up.html',{'form':form})
    else:
        form = PasswordMatch()
    return render(request,'sign_up.html',{'form':form})
    