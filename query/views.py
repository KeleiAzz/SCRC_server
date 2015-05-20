from django.shortcuts import render, redirect
from query.models import Company, Rating
from django.db.models import Q

from django.views.generic.edit import FormView
from query.forms import MultipleChoiceForm
# Create your views here.

def home_page(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

def company_details(request, id):
    if len(id) > 3:
        company = Company.objects.get(name=id)
    else:
        company = Company.objects.get(id=id)
    ratings = Rating.objects.all().filter(company_id=company.id).order_by('date', 'category_id')

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
    form = MultipleChoiceForm(request)
    if 'btn1' in request.POST:
        form = MultipleChoiceForm(request)
        if request.POST.get('selected', 0) != 0:
            selected_company = request.POST.get('selected').split('#')
            selected_company = list(set(selected_company))
            # selected_company = [i for i in selected]
            selected_company_name = [Company.objects.get(id=int(i)).name for i in selected_company]
            selected_details = {}
            for i in range(len(selected_company)):
                selected_details[selected_company_name[i]] = \
                    Rating.objects.all().filter(company_id=int(selected_company[i])).order_by('date','category_id')
        return render(request, 'advanced_search.html', {'form': form,
                                                        'choice_field': request.POST.getlist('choice_field', 0),
                                                        'selected_company_id': '#'.join(selected_company),
                                                        'selected_company_name': selected_company_name,
                                                        'selected_details': selected_details
                                                        })

    if 'btn2' in request.POST:
        if request.POST.get('selected', 0) != 0:
            selected = request.POST.get('selected').split('#')
            selected_company = selected


        if request.method == 'POST':
            selected_company += [str(i) for i in request.POST.getlist('choice_field')]
            selected_company = list(set(selected_company))
            if '' in selected_company:
                selected_company.remove('')
            selected_company_id = '#'.join(selected_company)
            selected_company_name = [Company.objects.get(id=int(i)).name for i in selected_company]
            selected_details = {}
            for i in range(len(selected_company)):
                selected_details[selected_company_name[i]] = \
                    Rating.objects.all().filter(company_id=int(selected_company[i])).order_by('date','category_id')

            return render(request, 'advanced_search.html', {'form': form,
                                                            'selected_company_name': selected_company_name,
                                                            'selected_details': selected_details,
                                                            'selected_company_id': selected_company_id,
                                                            })

    # if request.method == 'POST' and request.POST.getlist('choice_field', 0) == 0 :
    #     companies = Company.objects.filter(name__icontains=request.POST['company_name'])
    #     return redirect('/', {'companies': companies})
    return render(request, 'advanced_search.html', {'form': form, 'choice_field': request.POST.getlist('choice_field', 0) })

# class MultipleChoiceView(FormView):
#     template_name = 'advanced_search.html'
#     form_class = MultipleChoiceForm
#     success_url = '/advanced_search/'
