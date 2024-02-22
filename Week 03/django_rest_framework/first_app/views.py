from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework import filters
from . import paginations

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description']
    
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price']
    
    # pagination_class = paginations.ProductPagination
    # pagination_class = paginations.ProductLimitOffsetPagination
    pagination_class = paginations.ProductCursorPagination


# class ReviewFilterSet(rest_framework.FilterSet):
#     user__username = rest_framework.CharFilter(field_name='user__username', lookup_expr='icontains')


class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.ReviewerOrReadOnly]
    
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ReviewSerializer
    
    # def get_queryset(self):
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset
    
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username']
    # filterset_class = ReviewFilterSet
    
    filterset_fields = ['rating','product']
    
    # test
    
    
 