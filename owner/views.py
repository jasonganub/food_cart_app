from django.shortcuts import render
from .models import Owner, OpeningHours


def browse_trucks(request):
    if request.method == "GET":
        list_of_trucks = Owner.objects.all()
        context = {'list_of_trucks': list_of_trucks}
        return render(request, 'browse.html', context)
    else:
        pass
    return render(request, 'browse.html')
