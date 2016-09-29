from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].required = True
		self.fields['email'].required = True
		self.fields['password'].required = True
