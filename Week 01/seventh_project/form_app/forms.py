from django import forms 
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label="User Name: ", help_text="Name must be at max 20 character.", widget=forms.TextInput(attrs={'placeholder':'Enter your name.'}))
    email = forms.EmailField(label="User Email: ", initial="Email")
    file = forms.FileField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICE = [('S','Small'),('M','Medium'),('L','Large'),('XL','Extra Large')]
    size = forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    ITEM = [('T','Toppings'),('M','Mashroom'),('P','Papperoni')]
    pizza = forms.MultipleChoiceField(choices=ITEM,widget=forms.CheckboxSelectMultiple)
    comment = forms.CharField(widget=forms.Textarea(attrs={'id':'text_area','placeholder': 'Please enter your valueble comment.'}))
    
    
# class StudentData(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 character.")
#     #     return valname
    
#     # def clean_email(self):
#     #     emaill = self.cleaned_data['email']
#     #     if '.com' not in emaill:
#     #         raise forms.ValidationError("Email should be contain '.com'")
#     #     return emaill
    
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         emaill = self.cleaned_data['email']
        
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 character.")
        
#         if '.com' not in emaill:
#             raise forms.ValidationError("Email should be contain '.com'")
        
class StudentData(forms.Form):
    name = forms.CharField(widget= forms.TextInput, validators=[validators.MinLengthValidator(10,message="Enter a name with at least 10 character.")])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message ="Enter a valid email.")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(45,message="Age maximum 45 acceptable."),validators.MinValueValidator(25,message="Age at least 25 acceptable.")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message="File must be a pdf file.")])   
        
            

class PasswordMatch(forms.Form):
    name = forms.CharField() 
    password = forms.CharField(widget=forms.PasswordInput)    
    confirm_password = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        conf_pass = self.cleaned_data['confirm_password']
        
        if conf_pass != val_pass:
            raise forms.ValidationError("Password dosen't match.")
            
        
    
    
       