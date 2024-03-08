from django.contrib import admin
from .models import Product,ProductReview

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['id','product_name','slug','price','category','stock','created_date','modified_date','is_available']
    
admin.site.register(Product,AdminProduct)
admin.site.register(ProductReview)
    