from django.forms import ModelForm
from .models import Seeker
from django.contrib.auth.models import User

class SeekerModelForm(ModelForm):

    class Meta:
        model = Seeker
        fields = '__all__'
