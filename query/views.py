from django.shortcuts import render
from query.models import Company
# Create your views here.

def home_page(request):
    if request.method == "POST":
        companies = Company.objects.all().filter(name__icontains=request.POST['company_name'])
    else:
        companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

def company_details(request, id):
    company = Company.objects.get(id=id)
    return render(request, 'company_details.html', {'company': company})