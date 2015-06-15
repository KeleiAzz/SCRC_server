from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic.edit import CreateView, UpdateView
from models import Score, Evidence, Hypothesis, Factory
from forms import ScoreForm, CountryChoiceForm, EvidenceForm
from helpers import get_num_scales, get_overview, get_workers_num
from django.db.models import Sum
import random
import json
# Create your views here.
def score_create(request):
    form = Score
    return render(request, 'score_create_form.html', {'form': form})

def home(request):

    return render(request, 'home_page.html')

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
    if request.method == 'POST':
        country = request.POST.get('Select Country')
        country_form = CountryChoiceForm
        return redirect('/risk_evidence/supply_chain_impact/%s/' % (country))
    else:
        country_form = CountryChoiceForm
        hypothesis = [x.text for x in Hypothesis.objects.filter(category='SCI')]
        return render(request, 'sci_list.html', {
            # 'evidences': evidences,
            'hint': hypothesis,
            'country_form': country_form})

def sci_list_country(request, country):
    credibility, relevance, letter_scale = get_num_scales('SCI')
    hypothesis = [x.text for x in Hypothesis.objects.filter(category='SCI')]
    evidences = Evidence.objects.filter(country_id=country, category='SCI')

    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == 'NA':
                pass
            elif 'h' in field and len(field) < 4  and getattr(e, field) != 'NA':
                score = letter_scale[getattr(e, field)] * credibility[e.credibility] * relevance[e.relevance]
                setattr(e, field, round(score, 3))
    country_form = CountryChoiceForm
    return render(request, 'sci_list.html', {'evidences': evidences, 'hint': hypothesis, 'country': country, 'country_form': country_form})


def probability_list(request):
    if request.method == 'POST':
        country = request.POST.get('Select Country')
        country_form = CountryChoiceForm
        return redirect('/risk_evidence/probability/%s/' % (country))
    else:
        country_form = CountryChoiceForm
        hypothesis = [x.text for x in Hypothesis.objects.filter(category='P')]
        return render(request, 'probability_list.html', {
            # 'evidences': evidences,
            'hint': hypothesis,
            'country_form': country_form})

def probability_list_country(request, country):
    credibility, relevance, letter_scale = get_num_scales('P')
    hypothesis = [x.text for x in Hypothesis.objects.filter(category='P')]
    evidences = Evidence.objects.filter(country_id=country, category='P')
    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == 'NA':
                pass
            elif 'h' in field and len(field) < 4  and getattr(e, field) != 'NA':
                score = letter_scale[getattr(e, field)] * credibility[e.credibility] * relevance[e.relevance]
                setattr(e, field, round(score, 3))
    country_form = CountryChoiceForm
    return render(request, 'probability_list.html', {'evidences': evidences, 'hint': hypothesis, 'country': country, 'country_form': country_form})



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


def evidence_edit(request, e_id):
    instance = get_object_or_404(Evidence, id=e_id)

    form = EvidenceForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        country = instance.country
        if instance.category == "SCI":
            return redirect('/risk_evidence/supply_chain_impact/%s/' % country)
        else:
            return redirect('/risk_evidence/probability/%s/' % country)
    category = instance.category
    hypothesis = list(reversed([x.text for x in Hypothesis.objects.filter(category=category)]))
    form.fields['country'].widget.attrs['disabled'] = True
    form.fields['category'].widget.attrs['disabled'] = True
    return render(request, 'evidence_edit.html', {'form': form, "e_id": instance.id, 'hint': hypothesis})

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

    brief = Hypothesis.objects.filter(category="SCI").values("brief").order_by('num')

    hypothesis_brief = {}
    for i in range(23):
        hypothesis_brief['h%d' % (i+1)] = brief[i]

    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]
    footwear_data = []

    footwear_workers_by_country, footwear_workers_total = get_workers_num('FOOTWEAR')

    apparel_data = []

    apparel_workers_by_country, apparel_workers_total = get_workers_num('APPAREL')
    data = []
    for country in country_list:
        v = []
        f_v = []
        a_v = []
        no_overlap = {}
        for x in range(23):
            h = 'h%d' % (x+1)
            if probability_overview[country][x] > 0.01 and sci_overview[country][x] >= 0:
                if footwear_workers_by_country[country] > 0:
                    f_v.append({"y": probability_overview[country][x],
                                "x": sci_overview[country][x] * footwear_workers_by_country[country] / footwear_workers_total,
                                "shape": "circle", "size": random.random(), 'tooltip': h + ' - ' + hypothesis_brief[h]['brief']})

                a_v.append({"y": probability_overview[country][x],
                            "x": sci_overview[country][x] * apparel_workers_by_country[country] / apparel_workers_total,
                            "shape": "circle", "size": random.random(), 'tooltip': h + ' - ' + hypothesis_brief[h]['brief']})

                if (probability_overview[country][x], sci_overview[country][x]) not in no_overlap.keys():
                    no_overlap[(probability_overview[country][x], sci_overview[country][x])] = [h + ' - ' + hypothesis_brief[h]['brief']]
                else:
                    no_overlap[(probability_overview[country][x], sci_overview[country][x])].append(h + ' - ' + hypothesis_brief[h]['brief'])

        for key, value in no_overlap.iteritems():
            v.append({"y": key[0], "x": key[1], "shape": "circle", "size": random.random(), 'tooltip': ','.join(value)})

        data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': v,
                    }
        )
        footwear_data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': f_v,
                    }
        )
        apparel_data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': a_v,
                    }
        )
    if request.method == 'POST':
        if 'btn1' in request.POST:
            return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(data), 'type': 'Overall'})
        if 'btn2' in request.POST:
            return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(footwear_data), 'type': 'Footwear'})
        if 'btn3' in request.POST:
            return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(apparel_data), 'type': 'Apparel'})

    return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(data), 'type': 'Overall'})



def hypothesis_list(request):
    sci = [x.text for x in Hypothesis.objects.filter(category="SCI")]
    p = [x.text for x in Hypothesis.objects.filter(category="P")]
    return render(request, 'hypothesis_list.html', {'sci': sci, 'p': p})
