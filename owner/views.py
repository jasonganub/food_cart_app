from django.shortcuts import render


def browse_trucks(request):
    if request.method == "GET":
        pass
    else:
        pass
    return render(request, 'browse.html')
