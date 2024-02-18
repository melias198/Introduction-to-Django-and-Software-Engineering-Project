from django.urls import path
from . import views


urlpatterns = [
    # path('',views.HomeTemplate.as_view()),
    path('',views.set_cookie),
    path('get/',views.get_cookie),
    path('del/',views.delete_user_cookie),
    path('ses/',views.set_session),
    path('get_ses/',views.get_session),
    path('del_ses/',views.delete_session),
]
