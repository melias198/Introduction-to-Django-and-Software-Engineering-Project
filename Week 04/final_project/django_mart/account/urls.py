from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.user_update,name='edit_profile'),
    path('logout/',views.user_logout,name='logout'),
    path('order_history/',views.order_history,name='order_history'),
    path('order_details/<int:id>',views.order_details,name='order_details'),
    path('transactions_history/',views.transaction_history,name='transaction_history'),
    path('transaction_details/<int:id>',views.transaction_details,name='transaction_details'),
    path('completed_order/',views.order_complete,name='order_completed'),
]
