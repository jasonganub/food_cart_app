from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_seeker(request):
    return HttpResponse('<h1>Sign up</h1>')
