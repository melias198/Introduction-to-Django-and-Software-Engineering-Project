from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('rating/',views.rating, name="rating"),
    path('form/',views.django_form,name="form"),
    path('sign_up/',views.sign_up,name="sign_up"),
]
