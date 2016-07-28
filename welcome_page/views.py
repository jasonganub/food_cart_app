from django.shortcuts import render, redirect


def verify_authentication(request):
	if request.user.is_authenticated():
		#direct to welcome page if user is authenticated
		return render(request, 'welcome.html')
	else:
		#direct to landing page
		 return redirect('/')
