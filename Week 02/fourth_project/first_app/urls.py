from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('change_pass/',views.pass_change,name="pass_change"),
    path('change_pass2/',views.pass_change2,name="pass_change2"),
    path('logout/',views.user_logout,name="logout"),
    path('change_data/',views.user_change,name="data_change"),
]
