from django.shortcuts import render
from openinghours.models import Company, OpeningHours

#TODO: Create function to search and view detailed company
def display_all_companies(request):
    if request.method == "GET":
        companies = Company.objects.all()
        return render(request, 'companies.html', {'companies': companies})

def display_company_by_id(request):
    if request.method == "GET":
        pass
