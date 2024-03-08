from django.urls import path
from . import views

urlpatterns = [
    path('order_complete/',views.order_complete,name='order_complete'),
    path('checkout/',views.checkout,name='checkout'),
    path('success/',views.success_view,name='success'),
    path('payment/faild/',views.faild_view,name='faild'),
]
