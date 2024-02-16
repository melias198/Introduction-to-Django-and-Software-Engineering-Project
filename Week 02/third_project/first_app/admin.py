from django.contrib import admin
from first_app.models import ABC_Employee,ABC_Customer,Employee,Manager,HR,Friend,Me,Department,Student,Song,Album,Product,Customer
# Register your models here.


admin.site.register(ABC_Employee)
admin.site.register(ABC_Customer)

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','job_title']
    
@admin.register(Manager)
class Manager(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','job_title','salary']
    
@admin.register(HR)
class HR(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','job_title','salary']
    

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['school','section','present','hw']
    

@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ['school','section','present','hw']
    

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dep_id','dep_name']
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stud_id','stud_name','stud_contact','dep_id']
    

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id','title','artist']
    ordering = ['id']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','title','album']
    ordering = ['id']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','prod_id','prod_name']
    

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','cust_id','cust_name','product_info']