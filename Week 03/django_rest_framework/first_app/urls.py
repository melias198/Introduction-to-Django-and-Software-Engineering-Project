from django.urls import path,include
from rest_framework import routers
from .views import ProductViewSet,ReviewViewSet

router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('reviews',ReviewViewSet,basename='reviews')

urlpatterns = [
    path('',include(router.urls)),
    path('api_auth/', include('rest_framework.urls')),
]



