from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserModelForm, SeekerModelForm

def create_seeker(request):
    # if this is a POST request we need to process the user_form data
    if request.method == 'POST':
        # create a user_form instance and populate it with data from the request:
        #user_form = UserModelForm(request.POST)

        user_form = UserModelForm(request.POST)
        seeker_form = SeekerModelForm(request.POST)

      
        # check whether it's valid:
        if user_form.is_valid() and seeker_form.is_valid():
            # process the data in user_form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.

            user.set_password(user.password)
            user.save()

            seeker = seeker_form.save(commit=False)
            seeker.user = user

      
            seeker.save()
      
            return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank user_form
    else:
        user_form = UserModelForm()
        seeker_form = SeekerModelForm()

    return render(request, 'signup_page.html', {'user_form': user_form, 'seeker_form': seeker_form})
