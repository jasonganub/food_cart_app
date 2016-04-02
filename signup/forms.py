from django.forms import ModelForm
#from .models import Seeker
from django.contrib.auth.models import User
from django import forms

"""
class SeekerModelForm(ModelForm):

    class Meta:
        model = Seeker
        fields = '__all__'
"""

class UserModelForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username','first_name','last_name','password']