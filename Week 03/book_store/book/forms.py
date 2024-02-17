from django import forms
from book.models import BookStoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ['id','name','author','genre','page','price']
        
        labels = {
            'id':'Book ID',
            'name':'Book Name',
            'author':'Author Name',
        }