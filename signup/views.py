from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserModelForm

def create_seeker(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = UserModelForm(request.POST)

        form = UserModelForm(request.POST)

      
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            username, first_name, last_name, password = form.cleaned_data['username'], form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['password']
           

            user = User(username=username,first_name=first_name,last_name=last_name)



            user.set_password(password)
            user.save()
            
            #new_user.save()
            return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserModelForm()

    return render(request, 'signup.html', {'form': form})
