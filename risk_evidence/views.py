from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic.edit import CreateView, UpdateView
from models import Score, Evidence
from forms import ScoreForm, CountryChoiceForm, EvidenceForm
from helpers import get_num_scales
import random
import json
# Create your views here.

HINT = ["Enactment of local environmental compliance including water and waste disposal indicates negative "
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

# class ScoreCreate(UpdateView):
#     model = Score
#     fields = ['letter_scale']

def score_create(request):
    form = Score
    return render(request, 'score_create_form.html', {'form': form})

def home(request):

    return render(request,'home_page.html')

def score_list(request):
    scores = Score.objects.all()
    scores1 = Score.objects.all().filter(category='SCI').order_by('sub_category')
    scores2 = Score.objects.all().filter(category='P').order_by('sub_category')
    return render(request, 'score_list.html', {'scores1': scores1, 'form': ScoreForm, 'scores2': scores2})

def score_add(request):

    if request.method == 'POST':
        form = ScoreForm(request.POST)
        form.save()
        scores = Score.objects.all()
        return redirect('score_list')
    scores1 = Score.objects.all().filter(category='SCI').order_by('sub_category')
    scores2 = Score.objects.all().filter(category='P').order_by('sub_category')
    return render(request, 'score_add.html', {'scores1': scores1, 'form': ScoreForm, 'scores2': scores2})

def score_edit(request, score_id):
    scores = Score.objects.all()
    scores1 = Score.objects.all().filter(category='SCI').order_by('sub_category')
    scores2 = Score.objects.all().filter(category='P').order_by('sub_category')
    instance = get_object_or_404(Score, id=score_id)
    form = ScoreForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('score_list')
    return render(request, 'score_edit.html', {'scores1': scores1, 'scores2': scores2, 'form': form, "score_id": instance.id})

def sci_list(request):
    credibility, relevance, letter_scale = get_num_scales('SCI')

    if request.method == 'POST':
        evidences = Evidence.objects.filter(country_id=request.POST['Select Country'], category='SCI')
        country = request.POST['Select Country']
        country = country
    else:
        evidences = Evidence.objects.all()

    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == 'NA':
                pass
            elif 'h' in field and len(field) < 4  and getattr(e, field) != 'NA':
                score = letter_scale[getattr(e, field)] * credibility[e.credibility] * relevance[e.relevance]
                setattr(e, field, round(score, 3))


    if request.method == 'POST':
        country_form = CountryChoiceForm
        return render(request, 'sci_list.html', {'evidences': evidences, 'hint': HINT, 'country': country, 'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'sci_list.html', {
            # 'evidences': evidences,
            'hint': HINT,
            'country_form': country_form})

def probability_list(request):
    credibility, relevance, letter_scale = get_num_scales('P')

    if request.method == 'POST':
        evidences = Evidence.objects.filter(country_id=request.POST['Select Country'], category='P')
        country = request.POST['Select Country'].capitalize()
    else:
        evidences = Evidence.objects.all()

    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == 'NA':
                pass
            elif 'h' in field and len(field) < 4  and getattr(e, field) != 'NA':
                score = letter_scale[getattr(e, field)] * credibility[e.credibility] * relevance[e.relevance]
                setattr(e, field, round(score, 3))

    if request.method == 'POST':
        country_form = CountryChoiceForm
        return render(request, 'probability_list.html', {'evidences': evidences, 'hint': HINT, 'country': country,
                                                         'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'probability_list.html', {'hint': HINT, 'country_form': country_form})

def evidence_add(request):

    if request.method == 'POST':
        form1 = EvidenceForm(request.POST, prefix='form1')
        form2 = EvidenceForm(request.POST, prefix='form2')
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            if request.POST.get('category') == 'SCI':
                return redirect('sci_list')
            else:
                return redirect('probability_list')
    else:
        form1 = EvidenceForm(initial={'category': 'SCI'}, prefix='form1')
        form2 = EvidenceForm(initial={'category': 'P'}, prefix='form2')
    return render(request, 'evidence_add.html', {'form1': form1, 'form2': form2})

def overview(request):
    # For supply chain impact
    credibility, relevance, letter_scale = get_num_scales('SCI')

    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]
    # country_list.sort()
    hypothesis = []
    for i in range(1, 24, 1):
        hypothesis.append('h' + str(i))
    sci_overview = {}

    for country in country_list:
        sci_overview[country] = []
        for h in hypothesis:
            evidences = Evidence.objects.filter(country_id=country, category='SCI')
            score = 0
            for e in evidences:
                if getattr(e, h) == 'NA':
                    pass
                else:
                    score += letter_scale[getattr(e, h)] * credibility[e.credibility] * relevance[e.relevance]
            sci_overview[country].append(round(score, 3))

    # For probability
    credibility, relevance, letter_scale = get_num_scales('P')

    probability_overview = {}
    evidences_count = {}
    for country in country_list:
        probability_overview[country] = []
        evidences_count[country] = []
        for h in hypothesis:
            evidences_count[country].append(0)
            evidences = Evidence.objects.filter(country_id=country, category='P')
            score = 0
            for e in evidences:
                if getattr(e, h) == 'C C' or getattr(e, h) == 'C':
                    score += letter_scale[getattr(e, h)] * credibility[e.credibility] * relevance[e.relevance]
                if getattr(e, h) != 'NA':
                    evidences_count[country][-1] += 1
            probability_overview[country].append(score)
            if evidences_count[country][-1] == 0:
                evidences_count[country][-1] = 1

        for i in range(len(probability_overview[country])):

            probability_overview[country][i] = round(probability_overview[country][i]/(evidences_count[country][i] * credibility['High'] * relevance['High'] * letter_scale['C C']), 3)

    return render(request, 'overview.html', {'sci_overview': sci_overview, 'hint': HINT, 'p_overview': probability_overview})


def visual_map(request):
    credibility, relevance, letter_scale = get_num_scales('SCI')
    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]
    # country_list.sort()
    hypothesis = []
    for i in range(1, 24, 1):
        hypothesis.append('h' + str(i))
    sci_overview = {}

    for country in country_list:
        sci_overview[country] = []
        for h in hypothesis:
            evidences = Evidence.objects.filter(country_id=country, category='SCI')
            score = 0
            for e in evidences:
                if getattr(e, h) == 'NA':
                    pass
                else:
                    score += letter_scale[getattr(e, h)] * credibility[e.credibility] * relevance[e.relevance]
            sci_overview[country].append(round(score, 3))

    # For probability
    credibility, relevance, letter_scale = get_num_scales('P')

    probability_overview = {}
    evidences_count = {}
    for country in country_list:
        probability_overview[country] = []
        evidences_count[country] = []
        for h in hypothesis:
            evidences_count[country].append(0)
            evidences = Evidence.objects.filter(country_id=country, category='P')
            score = 0
            for e in evidences:
                if getattr(e, h) == 'C C' or getattr(e, h) == 'C':
                    score += letter_scale[getattr(e, h)] * credibility[e.credibility] * relevance[e.relevance]
                if getattr(e, h) != 'NA':
                    evidences_count[country][-1] += 1
            probability_overview[country].append(score)
            if evidences_count[country][-1] == 0:
                evidences_count[country][-1] = 1

        for i in range(len(probability_overview[country])):

            probability_overview[country][i] = round(probability_overview[country][i]/(evidences_count[country][i] * credibility['High'] * relevance['High'] * letter_scale['C C']), 3)

    data = []
    for country in country_list:
        v = []
        for x in range(23):
            if probability_overview[country][x] > 0.01 and sci_overview[country][x] >= 0:
                v.append({"y": probability_overview[country][x], "x": sci_overview[country][x], "shape": "circle",
                                    "size": random.random(), 'tooltip': 'h%d' % (x+1)})
        data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': v,
                    }
        )
    return render_to_response('visual_map.html', {'data_scatterchart_container': json.dumps(data)})