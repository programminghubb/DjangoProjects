from django import forms
from .models import SignUp

class SignupForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ('first_name','last_name', 'email', 'password')
