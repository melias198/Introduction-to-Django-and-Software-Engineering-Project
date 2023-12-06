from django.urls import path
from . import views

urlpatterns = [
    path('',views.common),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('course/',views.course),
]