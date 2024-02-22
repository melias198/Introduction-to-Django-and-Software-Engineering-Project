from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from . import permissions

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.ReviewerOrReadOnly]
    
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ReviewSerializer
    