from django.contrib import admin
from book.models import BookStoreModel
# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','author','genre','page','price','first_pub','last_pub')

admin.site.register(BookStoreModel,BookStoreModelAdmin)
