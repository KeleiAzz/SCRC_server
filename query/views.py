from django.shortcuts import render, redirect
from query.models import Company, Rating, Evidence, Secondary
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from query.forms import MultipleChoiceForm, CountryChoiceForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def home_page(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

@login_required(login_url='/query/login')
def company_details(request, id):
    # if len(id) > 3:
    company = Company.objects.get(name=id)
    # else:
    #     company = Company.objects.get(id=id)
    ratings = Rating.objects.all().filter(company_id=company.id).order_by('date', 'category_id')

    return render(request, 'company_details.html', {'company': company, 'ratings': ratings})

@login_required(login_url='/query/login')
def company_secondary(request, id):
    company = Company.objects.get(name=id)

    SRM = Secondary.objects.all().filter(company_id=company.id, section='SRM Evaluation')
    LHR = Secondary.objects.all().filter(company_id=company.id, section='LHR Evaluation')
    ES = Secondary.objects.all().filter(company_id=company.id, section='Environmental Sustainability Evaluation')
    # sections = ['SRM Evaluation', 'LHR Evaluation', 'Environmental Sustainability Evaluation']
    # for row in secondary:
    if len(SRM) + len(LHR) + len(ES) == 0:
        return render(request, 'secondary.html', {'no_data': 1, 'company': company.name})
    # SRM = []


    return render(request, 'secondary.html', {'SRM': SRM, 'LHR': LHR, 'ES': ES, 'company': company.name})

@login_required(login_url='/query/login')
def basic_search(request):
    companies_with_rating = Rating.objects.values_list('company_id', flat=True).distinct()
    if request.method == "POST":
        choice = request.POST.get('choice', 0)
        if choice == '3':
            companies = Company.objects.filter(Q(industry_group__icontains=request.POST['company_name']) &
                                               Q(id__in=companies_with_rating)).order_by('industry_group')
        if choice == '2':
            companies = Company.objects.filter(Q(bloomberg_ticker__icontains=request.POST['company_name']) &
                                               Q(id__in=companies_with_rating)).order_by('industry_group')

            # return render(request, 'basic_search.html', {'companies': companies})
        if choice == '1' or choice == 0:
            companies = Company.objects.filter(Q(name__icontains=request.POST['company_name']) &
                                               Q(id__in=companies_with_rating)).order_by('industry_group')
        industry = companies[0].industry_group
        grouped_companies = {industry: []}
        for company in companies:
            if company.industry_group == industry:
                grouped_companies[industry].append(company)
            else:
                grouped_companies[company.industry_group] = [company]
                industry = company.industry_group

        return render(request, 'basic_search.html', {'grouped_companyies': grouped_companies})
    else:
        # companies = Company.objects.filter(id__in=companies_with_rating).order_by('industry_group')
        return render(request, 'basic_search.html')




@login_required(login_url='/query/login')
def advanced_search(request):
    # form = MultipleChoiceForm(request)
    companies_with_rating = Rating.objects.values_list('company_id', flat=True).distinct()
    companies = Company.objects.filter(id__in=companies_with_rating).order_by('industry_group')


    industry = companies[0].industry_group
    grouped_companies = {industry: []}
    for company in companies:
        if company.industry_group == industry:
            grouped_companies[industry].append(company)
        else:
            grouped_companies[company.industry_group] = [company]
            industry = company.industry_group

    # if 'btn1' in request.POST:
    #     form = MultipleChoiceForm(request)
    #     if request.POST.get('selected', 0) != 0:
    #         selected_company = request.POST.get('selected').split('#')
    #         selected_company = list(set(selected_company))
    #         # selected_company = [i for i in selected]
    #         selected_company_name = [Company.objects.get(id=int(i)).name for i in selected_company]
    #         selected_details = {}
    #
    #
    #         for i in range(len(selected_company)):
    #             selected_details[selected_company_name[i]] = \
    #                 Rating.objects.all().filter(company_id=int(selected_company[i])).order_by('date','category_id')
    #     return render(request, 'advanced_search.html', {'form': form,
    #                                                     'choice_field': request.POST.getlist('choice_field', 0),
    #                                                     'selected_company_id': '#'.join(selected_company),
    #                                                     'selected_company_name': selected_company_name,
    #                                                     'selected_details': selected_details
    #                                                     })

    if 'btn2' in request.POST:
        # if request.POST.get('selected', 0) != 0:
        #     selected = request.POST.get('selected').split('#')
        #     selected_company = selected


        if request.method == 'POST':
            selected_company = request.POST.getlist('my-select')
            # selected_company = list(set(selected_company))
            # if '' in selected_company:
            #     selected_company.remove('')
            # selected_company_id = '#'.join(selected_company)
            selected_company_name = [Company.objects.get(id=i).name for i in selected_company]
            selected_details = {}

            for i in range(len(selected_company)):
                selected_details[selected_company_name[i]] = \
                    Rating.objects.all().filter(company_id=int(selected_company[i])).order_by('date','category_id')

            return render(request, 'advanced_search.html', {
                                                            'grouped_companies': grouped_companies,
                                                            'selected_company_name': selected_company_name,
                                                            'selected_details': selected_details,
                                                            # 'selected_company_id': selected_company_id,
                                                            })

    return render(request, 'advanced_search.html', {'grouped_companies': grouped_companies, 'choice_field': request.POST.getlist('choice_field', 0) })



def evidence_list(request):

    def get_score(level):
        if level == "HIGH":
            return 1.414
        if level == "MEDIUM":
            return 1
        if level == "LOW":
            return 0.707
    form = CountryChoiceForm
    if request.method == 'POST':
        evidences = Evidence.objects.filter(country__icontains=request.POST['country_name'])
        country = request.POST['country_name'].capitalize()
    else:
        evidences = Evidence.objects.all()
    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == -99:
                setattr(e, field, 'NA')
            elif len(field) < 4  and getattr(e, field) != -99:
                score = getattr(e, field) * get_score(e.credibility) * get_score(e.relevance)
                setattr(e, field, round(score, 3))

    hint = ["Enactment of local environmental compliance including water and waste disposal indicates negative "
            "supply chain impact",
            "Enactment of local regulation of chemical substance indicates negative supply chain impact",
            "Enactment of international regulation of chemical substance indicates negative supply chain impact",
            "Poor local water quality indicates negative supply chain impact",
            "Enactment of local restrictions related to building and fire safety indicates negative supply chain "
            "impact", "Local severance legislation issues indicates negative supply chain impact",
            "Local unrest over social welfare and other wage-related benefits indicates negative supply chain impact",
            "Local unrest over minimum wage issue indicates negative supply chain impact",
            "Lack of local power grid stability indicates negative supply chain impact",
            "Low local nutrition quality indicates negative supply chain impact",
            "Local talent shortage indicates negative supply chain impact",
            "Local child labor issues indicates negative supply chain impact",
            "Local HIV positive worker discrimination indicates negative supply chain impact",
            "Local migrant worker rights violation indicates negative supply chain impact",
            "Contractor implementation of information systems causing delay indicates negative supply chain impact",
            "Order variability indicates negative supply chain impact",
            "Poor contractor's financial health indicates negative supply chain impact",
            "Lack of product security indicates negative supply chain impact ",
            "Lack of transparency among supply chain members indicates negative supply chain impact",
            "Local political tension indicates negative supply chain impact",
            "International economic slowdown indicates negative supply chain impact",
            "Countrys geopolitical issues resulting in instability indicates negative supply chain impact",
            "Local flooding, typhoon or other weather issues indicates negative supply chain impact"]
    if request.method == 'POST':
        return render(request, 'evidence.html', {'evidences': evidences, 'hint': hint, 'country': country, 'form': form})
    else:
        return render(request, 'evidence.html', {'evidences': evidences, 'hint': hint, 'form': form})
# class MultipleChoiceView(FormView):
#     template_name = 'advanced_search.html'
#     form_class = MultipleChoiceForm
#     success_url = '/advanced_search/'
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/query/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

@login_required(login_url='/query/login')
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/query/')