from django import forms 
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        labels = {
            'roll':'Student Roll',
            'name':'Student Name',
        }
        
        help_texts = {
            'address':'Enter your full address'
        }
        
