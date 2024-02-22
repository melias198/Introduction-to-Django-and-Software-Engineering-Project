from django.contrib import admin
from .models import Product, ProductReview

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product','user', 'rating', 'created_at')  
    list_filter = ('product', 'rating') 
