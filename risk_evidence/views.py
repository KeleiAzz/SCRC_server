from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic.edit import CreateView, UpdateView
from models import Score, Evidence, Hypothesis
from forms import ScoreForm, CountryChoiceForm, EvidenceForm
from helpers import get_num_scales, get_overview
import random
import json
# Create your views here.
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
    hypothesis = [x.text for x in Hypothesis.objects.filter(category='SCI')]
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
        return render(request, 'sci_list.html', {'evidences': evidences, 'hint': hypothesis, 'country': country, 'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'sci_list.html', {
            # 'evidences': evidences,
            'hint': hypothesis,
            'country_form': country_form})

def probability_list(request):
    credibility, relevance, letter_scale = get_num_scales('P')
    hypothesis = [x.text for x in Hypothesis.objects.filter(category='P')]
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
        return render(request, 'probability_list.html', {'evidences': evidences, 'hint': hypothesis, 'country': country,
                                                         'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'probability_list.html', {'hint': hypothesis, 'country_form': country_form})

def evidence_add(request):
    hypothesis1 = list(reversed([x.text for x in Hypothesis.objects.filter(category='SCI')]))
    hypothesis2 = list(reversed([x.text for x in Hypothesis.objects.filter(category='P')]))
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
    return render(request, 'evidence_add.html', {'form1': form1, 'form2': form2, 'hint1': hypothesis1, 'hint2':hypothesis2})

def overview(request):
    # For supply chain impact
    hypothesis1 = [x.text for x in Hypothesis.objects.filter(category='SCI')]
    hypothesis2 = [x.text for x in Hypothesis.objects.filter(category='P')]
    sci_overview = get_overview("SCI")
    # For probability
    probability_overview = get_overview('P')
    return render(request, 'overview.html', {'sci_overview': sci_overview, 'hint1': hypothesis1, 'hint2':hypothesis2, 'p_overview': probability_overview})


def visual_map(request):
    sci_overview = get_overview("SCI")
    # For probability
    probability_overview = get_overview('P')
    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]
    data = []
    for country in country_list:
        v = []
        no_overlap = {}
        for x in range(23):
            if probability_overview[country][x] > 0.01 and sci_overview[country][x] >= 0:
                if (probability_overview[country][x], sci_overview[country][x]) not in no_overlap.keys():
                    no_overlap[(probability_overview[country][x], sci_overview[country][x])] = ['h%d' % (x+1)]
                else:
                    no_overlap[(probability_overview[country][x], sci_overview[country][x])].append('h%d' % (x+1))

        for key, value in no_overlap.iteritems():
            v.append({"y": key[0], "x": key[1], "shape": "circle", "size": random.random(), 'tooltip': ','.join(value)})

        data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': v,
                    }
        )
    return render_to_response('visual_map.html', {'data_scatterchart_container': json.dumps(data)})

def hypothesis_list(request):
    sci = [x.text for x in Hypothesis.objects.filter(category="SCI")]
    p = [x.text for x in Hypothesis.objects.filter(category="P")]
    return render(request, 'hypothesis_list.html', {'sci': sci, 'p': p})
