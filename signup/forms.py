from django import forms
from .models import Seeker
from django.contrib.auth.models import User

class SeekerModelForm(forms.ModelForm):

    class Meta:

        model = User
        fields = '__all__' 