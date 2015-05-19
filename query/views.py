from django.shortcuts import render, redirect
from query.models import Company, Rating
from django.db.models import Q
# Create your views here.

def home_page(request):
    if request.method == "POST":
        choice = request.POST.get('choice', 0)
        if choice == '2':
            companies = Company.objects.filter(Q(bloomberg_ticker__icontains=request.POST['company_name']) |
                                               Q(ticker__icontains=request.POST['company_name']))
            return render(request, 'home.html', {'companies': companies})
        if choice == '1' or choice == 0:
            companies = Company.objects.filter(name__icontains=request.POST['company_name'])

    else:
        companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

def company_details(request, id):
    company = Company.objects.get(id=id)
    ratings = Rating.objects.all().filter(company_id=id).order_by('date', 'category_id')

    return render(request, 'company_details.html', {'company': company, 'ratings': ratings})

def basic_search(request):
    if request.method == "POST":
        choice = request.POST.get('choice', 0)
        if choice == '2':
            companies = Company.objects.filter(Q(bloomberg_ticker__icontains=request.POST['company_name']) |
                                               Q(ticker__icontains=request.POST['company_name']))
            # return render(request, 'basic_search.html', {'companies': companies})
        if choice == '1' or choice == 0:
            companies = Company.objects.filter(name__icontains=request.POST['company_name'])

    else:
        companies = Company.objects.all()
    return render(request, 'basic_search.html', {'companies': companies})

def advanced_search(request):
    return render(request, 'advanced_search.html')