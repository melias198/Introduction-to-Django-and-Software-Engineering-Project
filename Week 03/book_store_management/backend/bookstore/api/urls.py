from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    # API View
    # path('books/', views.BookListAPI.as_view()),
    # path('books/<int:pk>/', views.BookDetailAPI.as_view()),
    
    # Generic Class View
    # path('books/', views.BookListGeneric.as_view()),
    # path('books/<int:pk>/', views.BookDetailGeneric.as_view()),
    
    # Model View Set
    path('',include(router.urls)),
]
