from django.db import models

# Create your models here.

# Model inheritance
# 1. Abstract Base Class 
# 2. Multi-Table Inheritance
# 3. Proxy Models

# 1. Abstract Base Class
class AbstractPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        abstract = True
        
        
class ABC_Employee(AbstractPerson):
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    

class ABC_Customer(AbstractPerson):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    
    
# 2. Multi-Table Inheritance
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    job_title = models.CharField(max_length=100)

class Manager(Employee):
    salary = models.IntegerField()

class HR(Employee):
    salary = models.IntegerField()
    

# 3. Proxy Model
class Friend(models.Model):
    school = models.CharField(max_length = 100)
    section = models.CharField(max_length = 10)
    present = models.BooleanField()
    hw = models.BooleanField()

class Me(Friend):
    class Meta:
        proxy = True

# Relationship
# 1. One To One 
# 2. One To Many
# 3. Many To Many

# 1. One To One
class Department(models.Model):
    dep_id= models.IntegerField()
    dep_name= models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.dep_id)
    
class Student(models.Model):
    stud_id= models.IntegerField()
    stud_name= models.CharField(max_length = 100)
    stud_contact= models.IntegerField()
    dep_id= models.OneToOneField(Department, on_delete = models.CASCADE, primary_key = True)
    

# 2. One To Many
class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title
  
class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    

# 3. Many To Many
class Product(models.Model):
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.prod_name

class Customer(models.Model):
    cust_id = models.IntegerField()
    cust_name = models.CharField(max_length = 100)
    prod = models.ManyToManyField(Product)
    
    def product_info(self):
        return ",".join([str(i) for i in self.prod.all()])