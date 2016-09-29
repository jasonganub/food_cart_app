from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register_user(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			new_user = authenticate(username=new_user.username, password=new_user.password)
			if new_user:
				login(request, new_user)
				# redirect, or however you want to get to the main view
				return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'registration.html', {'form': form})
