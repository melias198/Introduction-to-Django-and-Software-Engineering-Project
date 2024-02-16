from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 30)
    roll = models.IntegerField(primary_key = True)
    address = models.TextField()
    phone = models.TextField(blank = True)
    
    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"