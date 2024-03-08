from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=255,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    

class ProductReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=552)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    
    