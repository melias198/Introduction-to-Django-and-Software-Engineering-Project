from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime,timedelta
from django.http import HttpResponse

# Create your views here.
# class HomeTemplate(TemplateView):
#     template_name = 'home.html'
    
def set_cookie(request):
    response = render(request,'cookie.html')
    response.set_cookie('name','elias')
    # response.set_cookie('name','elias', max_age=10)
    response.set_cookie('name','elias', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})


def delete_user_cookie(request):
    response = render(request,'home.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name':'Elias',
        'age':23,
        'language':'Bangla',
    }
    request.session.update(data)
    return render(request,'session.html')


# def get_session(request):
#     data = request.session
#     return render(request,'get_session.html',{'data':data})


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name')
        request.session.modified = True
        return render(request,'get_session.html',{'data':name})
    else:
        return HttpResponse("You session has been expired!")
        


def delete_session(request):
    request.session.flush()
    return render(request,'del_seeion.html')