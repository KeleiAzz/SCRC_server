from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic.edit import CreateView, UpdateView
from models import Score, Evidence
from forms import ScoreForm, CountryChoiceForm, EvidenceForm
import random, time, datetime
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

    # data = [
    #     {
    #         'key': '',
    #         'value':[
    #
    #         ],
    #     }
    # ]
    data_scatterchart_container=[{"values": [{"y": 0, "x": 3, "shape": "circle", "size": 1}, {"y": 7, "x": 9, "shape": "circle", "size": 1},
        {"y": 18, "x": 4, "shape": "circle", "size": 1}, {"y": 30, "x": 10, "shape": "circle", "size": 1}, {"y": 24, "x": 14, "shape": "circle", "size": 1},
        {"y": 30, "x": 14, "shape": "circle", "size": 1}, {"y": 36, "x": 14, "shape": "circle", "size": 1}, {"y": 42, "x": 16, "shape": "circle", "size": 1},
        {"y": 80, "x": 10, "shape": "circle", "size": 1}, {"y": 72, "x": 12, "shape": "circle", "size": 1}, {"y": 60, "x": 15, "shape": "circle", "size": 1},
        {"y": 55, "x": 13, "shape": "circle", "size": 1}, {"y": 120, "x": 17, "shape": "circle", "size": 1}, {"y": 13, "x": 16, "shape": "circle", "size": 1},
        {"y": 42, "x": 17, "shape": "circle", "size": 1}, {"y": 90, "x": 24, "shape": "circle", "size": 1}, {"y": 32, "x": 18, "shape": "circle", "size": 1},
        {"y": 119, "x": 20, "shape": "circle", "size": 1}, {"y": 180, "x": 22, "shape": "circle", "size": 1}, {"y": 76, "x": 26, "shape": "circle", "size": 1},
        {"y": 140, "x": 25, "shape": "circle", "size": 1}, {"y": 189, "x": 26, "shape": "circle", "size": 1}, {"y": 198, "x": 27, "shape": "circle", "size": 1},
        {"y": 161, "x": 27, "shape": "circle", "size": 1}, {"y": 240, "x": 25, "shape": "circle", "size": 1}, {"y": 75, "x": 32, "shape": "circle", "size": 1},
        {"y": 182, "x": 33, "shape": "circle", "size": 1}, {"y": 27, "x": 33, "shape": "circle", "size": 1}, {"y": 84, "x": 29, "shape": "circle", "size": 1},
        {"y": 174, "x": 39, "shape": "circle", "size": 1}, {"y": 150, "x": 36, "shape": "circle", "size": 1}, {"y": 217, "x": 37, "shape": "circle", "size": 1},
        {"y": 160, "x": 38, "shape": "circle", "size": 1}, {"y": 330, "x": 42, "shape": "circle", "size": 1}, {"y": 272, "x": 39, "shape": "circle", "size": 1},
        {"y": 245, "x": 43, "shape": "circle", "size": 1}, {"y": 108, "x": 45, "shape": "circle", "size": 1}, {"y": 185, "x": 47, "shape": "circle", "size": 1},
        {"y": 190, "x": 46, "shape": "circle", "size": 1}, {"y": 273, "x": 48, "shape": "circle", "size": 1}, {"y": 80, "x": 47, "shape": "circle", "size": 1}, {"y": 164, "x": 48, "shape": "circle", "size": 1}, {"y": 84, "x": 50, "shape": "circle", "size": 1}, {"y": 387, "x": 53, "shape": "circle", "size": 1}, {"y": 132, "x": 50, "shape": "circle", "size": 1}, {"y": 135, "x": 47, "shape": "circle", "size": 1}, {"y": 184, "x": 50, "shape": "circle", "size": 1}, {"y": 94, "x": 54, "shape": "circle", "size": 1}, {"y": 432, "x": 56, "shape": "circle", "size": 1}, {"y": 343, "x": 53, "shape": "circle", "size": 1}], "key": "series 1", "yAxis": "1"}, {"values": [{"y": 0, "x": 3, "shape": "cross", "size": 1}, {"y": 14, "x": 9, "shape": "cross", "size": 1}, {"y": 36, "x": 4, "shape": "cross", "size": 1}, {"y": 60, "x": 10, "shape": "cross", "size": 1}, {"y": 48, "x": 14, "shape": "cross", "size": 1}, {"y": 60, "x": 14, "shape": "cross", "size": 1}, {"y": 72, "x": 14, "shape": "cross", "size": 1}, {"y": 84, "x": 16, "shape": "cross", "size": 1}, {"y": 160, "x": 10, "shape": "cross", "size": 1}, {"y": 144, "x": 12, "shape": "cross", "size": 1}, {"y": 120, "x": 15, "shape": "cross", "size": 1}, {"y": 110, "x": 13, "shape": "cross", "size": 1}, {"y": 240, "x": 17, "shape": "cross", "size": 1}, {"y": 26, "x": 16, "shape": "cross", "size": 1}, {"y": 84, "x": 17, "shape": "cross", "size": 1}, {"y": 180, "x": 24, "shape": "cross", "size": 1}, {"y": 64, "x": 18, "shape": "cross", "size": 1}, {"y": 238, "x": 20, "shape": "cross", "size": 1}, {"y": 360, "x": 22, "shape": "cross", "size": 1}, {"y": 152, "x": 26, "shape": "cross", "size": 1}, {"y": 280, "x": 25, "shape": "cross", "size": 1}, {"y": 378, "x": 26, "shape": "cross", "size": 1}, {"y": 396, "x": 27, "shape": "cross", "size": 1}, {"y": 322, "x": 27, "shape": "cross", "size": 1}, {"y": 480, "x": 25, "shape": "cross", "size": 1}, {"y": 150, "x": 32, "shape": "cross", "size": 1}, {"y": 364, "x": 33, "shape": "cross", "size": 1}, {"y": 54, "x": 33, "shape": "cross", "size": 1}, {"y": 168, "x": 29, "shape": "cross", "size": 1}, {"y": 348, "x": 39, "shape": "cross", "size": 1}, {"y": 300, "x": 36, "shape": "cross", "size": 1}, {"y": 434, "x": 37, "shape": "cross", "size": 1}, {"y": 320, "x": 38, "shape": "cross", "size": 1}, {"y": 660, "x": 42, "shape": "cross", "size": 1}, {"y": 544, "x": 39, "shape": "cross", "size": 1}, {"y": 490, "x": 43, "shape": "cross", "size": 1}, {"y": 216, "x": 45, "shape": "cross", "size": 1}, {"y": 370, "x": 47, "shape": "cross", "size": 1}, {"y": 380, "x": 46, "shape": "cross", "size": 1}, {"y": 546, "x": 48, "shape": "cross", "size": 1}, {"y": 160, "x": 47, "shape": "cross", "size": 1}, {"y": 328, "x": 48, "shape": "cross", "size": 1}, {"y": 168, "x": 50, "shape": "cross", "size": 1}, {"y": 774, "x": 53, "shape": "cross", "size": 1}, {"y": 264, "x": 50, "shape": "cross", "size": 1}, {"y": 270, "x": 47, "shape": "cross", "size": 1}, {"y": 368, "x": 50, "shape": "cross", "size": 1}, {"y": 188, "x": 54, "shape": "cross", "size": 1}, {"y": 864, "x": 56, "shape": "cross", "size": 1}, {"y": 686, "x": 53, "shape": "cross", "size": 1}], "key": "series 2", "yAxis": "1"}, {"values": [{"y": 0, "x": 3, "shape": "triangle-up", "size": 1}, {"y": 35, "x": 9, "shape": "triangle-up", "size": 1}, {"y": 90, "x": 4, "shape": "triangle-up", "size": 1}, {"y": 150, "x": 10, "shape": "triangle-up", "size": 1}, {"y": 120, "x": 14, "shape": "triangle-up", "size": 1}, {"y": 150, "x": 14, "shape": "triangle-up", "size": 1}, {"y": 180, "x": 14, "shape": "triangle-up", "size": 1}, {"y": 210, "x": 16, "shape": "triangle-up", "size": 1}, {"y": 400, "x": 10, "shape": "triangle-up", "size": 1}, {"y": 360, "x": 12, "shape": "triangle-up", "size": 1}, {"y": 300, "x": 15, "shape": "triangle-up", "size": 1}, {"y": 275, "x": 13, "shape": "triangle-up", "size": 1}, {"y": 600, "x": 17, "shape": "triangle-up", "size": 1}, {"y": 65, "x": 16, "shape": "triangle-up", "size": 1}, {"y": 210, "x": 17, "shape": "triangle-up", "size": 1}, {"y": 450, "x": 24, "shape": "triangle-up", "size": 1}, {"y": 160, "x": 18, "shape": "triangle-up", "size": 1}, {"y": 595, "x": 20, "shape": "triangle-up", "size": 1}, {"y": 900, "x": 22, "shape": "triangle-up", "size": 1}, {"y": 380, "x": 26, "shape": "triangle-up", "size": 1}, {"y": 700, "x": 25, "shape": "triangle-up", "size": 1}, {"y": 945, "x": 26, "shape": "triangle-up", "size": 1}, {"y": 990, "x": 27, "shape": "triangle-up", "size": 1}, {"y": 805, "x": 27, "shape": "triangle-up", "size": 1}, {"y": 1200, "x": 25, "shape": "triangle-up", "size": 1}, {"y": 375, "x": 32, "shape": "triangle-up", "size": 1}, {"y": 910, "x": 33, "shape": "triangle-up", "size": 1}, {"y": 135, "x": 33, "shape": "triangle-up", "size": 1}, {"y": 420, "x": 29, "shape": "triangle-up", "size": 1}, {"y": 870, "x": 39, "shape": "triangle-up", "size": 1}, {"y": 750, "x": 36, "shape": "triangle-up", "size": 1}, {"y": 1085, "x": 37, "shape": "triangle-up", "size": 1}, {"y": 800, "x": 38, "shape": "triangle-up", "size": 1}, {"y": 1650, "x": 42, "shape": "triangle-up", "size": 1}, {"y": 1360, "x": 39, "shape": "triangle-up", "size": 1}, {"y": 1225, "x": 43, "shape": "triangle-up", "size": 1}, {"y": 540, "x": 45, "shape": "triangle-up", "size": 1}, {"y": 925, "x": 47, "shape": "triangle-up", "size": 1}, {"y": 950, "x": 46, "shape": "triangle-up", "size": 1}, {"y": 1365, "x": 48, "shape": "triangle-up", "size": 1}, {"y": 400, "x": 47, "shape": "triangle-up", "size": 1}, {"y": 820, "x": 48, "shape": "triangle-up", "size": 1}, {"y": 420, "x": 50, "shape": "triangle-up", "size": 1}, {"y": 1935, "x": 53, "shape": "triangle-up", "size": 1}, {"y": 660, "x": 50, "shape": "triangle-up", "size": 1}, {"y": 675, "x": 47, "shape": "triangle-up", "size": 1}, {"y": 920, "x": 50, "shape": "triangle-up", "size": 1}, {"y": 470, "x": 54, "shape": "triangle-up", "size": 1}, {"y": 2160, "x": 56, "shape": "triangle-up", "size": 1}, {"y": 1715, "x": 53, "shape": "triangle-up", "size": 1}], "key": "series 3", "yAxis": "1"}];


    return render_to_response('home_page.html', {'data_scatterchart_container': json.dumps(data_scatterchart_container)})

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

    credibility = {}
    credibility['High'] = Score.objects.get(letter_scale='High', category='SCI', sub_category='Credibility').num_scale
    credibility['Medium'] = Score.objects.get(letter_scale='Medium', category='SCI', sub_category='Credibility').num_scale
    credibility['Low'] = Score.objects.get(letter_scale='Low', category='SCI', sub_category='Credibility').num_scale

    relevance = {}
    relevance['High'] = Score.objects.get(letter_scale='High', category='SCI', sub_category='Relevance').num_scale
    relevance['Medium'] = Score.objects.get(letter_scale='Medium', category='SCI', sub_category='Relevance').num_scale
    relevance['Low'] = Score.objects.get(letter_scale='Low', category='SCI', sub_category='Relevance').num_scale

    letter_scale = {}
    letter_scale['I I'] = Score.objects.get(letter_scale='I I', category='SCI').num_scale
    letter_scale['I'] = Score.objects.get(letter_scale='I', category='SCI').num_scale
    letter_scale['NA'] = Score.objects.get(letter_scale='NA', category='SCI').num_scale
    letter_scale['N'] = Score.objects.get(letter_scale='N', category='SCI').num_scale
    letter_scale['C'] = Score.objects.get(letter_scale='C', category='SCI').num_scale
    letter_scale['C C'] = Score.objects.get(letter_scale='C C', category='SCI').num_scale

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
        return render(request, 'evidence_list.html', {'evidences': evidences, 'hint': HINT, 'country': country, 'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'evidence_list.html', {
            # 'evidences': evidences,
            'hint': HINT,
            'country_form': country_form})

def probability_list(request):
    credibility = {}
    credibility['High'] = Score.objects.get(letter_scale='High', category='P', sub_category='Credibility').num_scale
    credibility['Medium'] = Score.objects.get(letter_scale='Medium', category='P', sub_category='Credibility').num_scale
    credibility['Low'] = Score.objects.get(letter_scale='Low', category='P', sub_category='Credibility').num_scale

    relevance = {}
    relevance['High'] = Score.objects.get(letter_scale='High', category='P', sub_category='Relevance').num_scale
    relevance['Medium'] = Score.objects.get(letter_scale='Medium', category='P', sub_category='Relevance').num_scale
    relevance['Low'] = Score.objects.get(letter_scale='Low', category='P', sub_category='Relevance').num_scale

    letter_scale = {}
    letter_scale['I I'] = Score.objects.get(letter_scale='I I', category='P').num_scale
    letter_scale['I'] = Score.objects.get(letter_scale='I', category='P').num_scale
    letter_scale['NA'] = Score.objects.get(letter_scale='NA', category='P').num_scale
    letter_scale['N'] = Score.objects.get(letter_scale='N', category='P').num_scale
    letter_scale['C'] = Score.objects.get(letter_scale='C', category='P').num_scale
    letter_scale['C C'] = Score.objects.get(letter_scale='C C', category='P').num_scale

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
        return render(request, 'probability_list.html', { 'hint': HINT,'country_form': country_form})

def evidence_add(request):
    if request.method == 'POST':
        form = EvidenceForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('category') == 'SCI':
                return redirect('sci_list')
            else:
                return redirect('probability_list')

    form = EvidenceForm()
    return render(request, 'evidence_add.html', {'form': form})

def overview(request):
    # For supply chain impact
    credibility = {}
    credibility['High'] = Score.objects.get(letter_scale='High', category='SCI', sub_category='Credibility').num_scale
    credibility['Medium'] = Score.objects.get(letter_scale='Medium', category='SCI', sub_category='Credibility').num_scale
    credibility['Low'] = Score.objects.get(letter_scale='Low', category='SCI', sub_category='Credibility').num_scale

    relevance = {}
    relevance['High'] = Score.objects.get(letter_scale='High', category='SCI', sub_category='Relevance').num_scale
    relevance['Medium'] = Score.objects.get(letter_scale='Medium', category='SCI', sub_category='Relevance').num_scale
    relevance['Low'] = Score.objects.get(letter_scale='Low', category='SCI', sub_category='Relevance').num_scale

    letter_scale = {}
    letter_scale['I I'] = Score.objects.get(letter_scale='I I', category='SCI').num_scale
    letter_scale['I'] = Score.objects.get(letter_scale='I', category='SCI').num_scale
    letter_scale['NA'] = Score.objects.get(letter_scale='NA', category='SCI').num_scale
    letter_scale['N'] = Score.objects.get(letter_scale='N', category='SCI').num_scale
    letter_scale['C'] = Score.objects.get(letter_scale='C', category='SCI').num_scale
    letter_scale['C C'] = Score.objects.get(letter_scale='C C', category='SCI').num_scale

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
            sci_overview[country].append(round(score,3))

    # For probability
    credibility = {}
    credibility['High'] = Score.objects.get(letter_scale='High', category='P', sub_category='Credibility').num_scale
    credibility['Medium'] = Score.objects.get(letter_scale='Medium', category='P', sub_category='Credibility').num_scale
    credibility['Low'] = Score.objects.get(letter_scale='Low', category='P', sub_category='Credibility').num_scale

    relevance = {}
    relevance['High'] = Score.objects.get(letter_scale='High', category='P', sub_category='Relevance').num_scale
    relevance['Medium'] = Score.objects.get(letter_scale='Medium', category='P', sub_category='Relevance').num_scale
    relevance['Low'] = Score.objects.get(letter_scale='Low', category='P', sub_category='Relevance').num_scale

    letter_scale = {}
    letter_scale['I I'] = Score.objects.get(letter_scale='I I', category='P').num_scale
    letter_scale['I'] = Score.objects.get(letter_scale='I', category='P').num_scale
    letter_scale['NA'] = Score.objects.get(letter_scale='NA', category='P').num_scale
    letter_scale['N'] = Score.objects.get(letter_scale='N', category='P').num_scale
    letter_scale['C'] = Score.objects.get(letter_scale='C', category='P').num_scale
    letter_scale['C C'] = Score.objects.get(letter_scale='C C', category='P').num_scale

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


