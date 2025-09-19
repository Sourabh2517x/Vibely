from django import forms
from django.contrib.auth.models import User  # --> user is inbuilt model of django
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:                             # --> Meta class hold the information of above form/class
        model = User                        # --> which model this form use
        fields = ['username','email','password1','password2']