from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_datil,name='product_detail'),
    path('search/',views.search_view,name='search_by_product'),
]
