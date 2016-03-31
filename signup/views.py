from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
#def create_seeker(request):
    #return HttpResponse('<h1>Sign up</h1>')





def create_seeker(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = User(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = User()

    return render(request, 'signup.html', {'form': form})
    
