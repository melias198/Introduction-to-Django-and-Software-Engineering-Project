from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 15)
    address = models.TextField(max_length = 50)
    
    def __str__(self):
        return self.name