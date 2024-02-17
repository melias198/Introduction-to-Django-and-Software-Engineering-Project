from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    GENRE = (
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi','Sci-Fi'),
        ('Romantic','Romantic'),
        ('Islamic','Islamic'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    genre = models.CharField(max_length = 30,choices = GENRE)
    page = models.IntegerField()
    price = models.IntegerField()
    first_pub = models.DateTimeField(auto_now_add = True)
    last_pub = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"Book : {self.name} -- Author : {self.author}"