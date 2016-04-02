from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import SeekerModelForm, UserModelForm

def create_seeker(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserModelForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserModelForm()

    return render(request, 'signup.html', {'form': form})
