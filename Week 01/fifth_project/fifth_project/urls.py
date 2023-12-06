
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.nevbar),
    path('home/',include('home_app.urls')),
    path('about/',include('about_app.urls')),
    path('contact/',include('contact_app.urls')),
    path('course/',include('course_app.urls')),
]
