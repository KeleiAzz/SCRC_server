from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic.edit import CreateView, UpdateView
from models import Score, Evidence, Hypothesis, Factory
from forms import ScoreForm, CountryChoiceForm, EvidenceForm
from helpers import get_num_scales, get_overview, get_workers_num
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import random
import json

# Create your views here.
@login_required(login_url='/risk_evidence/login')
def score_create(request):
    form = Score
    return render(request, 'score_create_form.html', {'form': form})

def home(request):
    return render(request, 'home_page.html')

@login_required(login_url='/risk_evidence/login')
def score_list(request):
    scores = Score.objects.all()
    scores1 = Score.objects.all().filter(category='SCI').order_by('sub_category')
    scores2 = Score.objects.all().filter(category='P').order_by('sub_category')
    return render(request, 'score_list.html', {'scores1': scores1, 'form': ScoreForm, 'scores2': scores2})

@login_required(login_url='/risk_evidence/login')
def score_add(request):

    if request.method == 'POST':
        form = ScoreForm(request.POST)
        form.save()
        scores = Score.objects.all()
        return redirect('score_list')
    scores1 = Score.objects.all().filter(category='SCI').order_by('sub_category')
    scores2 = Score.objects.all().filter(category='P').order_by('sub_category')
    return render(request, 'score_add.html', {'scores1': scores1, 'form': ScoreForm, 'scores2': scores2})

@login_required(login_url='/risk_evidence/login')
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

@login_required(login_url='/risk_evidence/login')
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

@login_required(login_url='/risk_evidence/login')
def sci_list_country(request, country):
    credibility, relevance, letter_scale = get_num_scales('SCI')
    hypothesis = [x.text for x in Hypothesis.objects.filter(category='SCI')]
    evidences = Evidence.objects.filter(country_id=country, category='SCI')

    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == 'NA':
                pass
            elif 'h' in field and len(field) < 4  and getattr(e, field) != 'NA':
                score = letter_scale[getattr(e, field).upper()] * credibility[e.credibility.capitalize()] * relevance[e.relevance.capitalize()]
                setattr(e, field, round(score, 3))
    country_form = CountryChoiceForm
    return render(request, 'sci_list.html', {'evidences': evidences, 'hint': hypothesis, 'country': country, 'country_form': country_form})

@login_required(login_url='/risk_evidence/login')
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

@login_required(login_url='/risk_evidence/login')
def probability_list_country(request, country):
    credibility, relevance, letter_scale = get_num_scales('P')
    hypothesis = [x.text for x in Hypothesis.objects.filter(category='P')]
    evidences = Evidence.objects.filter(country_id=country, category='P')
    for e in evidences:
        for field in e._meta.get_all_field_names():
            if len(field) < 4 and getattr(e, field) == 'NA':
                pass
            elif 'h' in field and len(field) < 4  and getattr(e, field) != 'NA':
                score = letter_scale[getattr(e, field).upper()] * credibility[e.credibility.capitalize()] * relevance[e.relevance.capitalize()]
                setattr(e, field, round(score, 3))
    country_form = CountryChoiceForm
    return render(request, 'probability_list.html', {'evidences': evidences, 'hint': hypothesis, 'country': country, 'country_form': country_form})

@login_required(login_url='/risk_evidence/login')
def evidence_add(request):
    hypothesis1 = list(reversed([x.text for x in Hypothesis.objects.filter(category='SCI')]))
    hypothesis2 = list(reversed([x.text for x in Hypothesis.objects.filter(category='P')]))
    if request.method == 'POST':
        if 'btn2' in request.POST:
            form1 = EvidenceForm(initial={'category': 'SCI', 'country': request.POST['country_to_add']}, prefix='form1')
            form2 = EvidenceForm(initial={'category': 'P', 'country': request.POST['country_to_add']}, prefix='form2')
            return render(request, 'evidence_add.html', {'form1': form1, 'form2': form2, 'hint1': hypothesis1, 'hint2':hypothesis2})

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

@login_required(login_url='/risk_evidence/login')
def evidence_edit(request, e_id):
    instance = get_object_or_404(Evidence, id=e_id)
    if request.method == "POST" and 'btn2' in request.POST:
        country = instance.country
        category = instance.category
        Evidence.objects.get(id=e_id).delete()
        if category == "SCI":
            return redirect('/risk_evidence/supply_chain_impact/%s/' % country)
        else:
            return redirect('/risk_evidence/probability/%s/' % country)

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
    form.fields['country'].widget.attrs['readonly'] = True
    form.fields['category'].widget.attrs['readonly'] = True
    return render(request, 'evidence_edit.html', {'form': form, "e_id": instance.id, 'hint': hypothesis})

@login_required(login_url='/risk_evidence/login')
def overview(request):
    # For supply chain impact
    hypothesis1 = [x.text for x in Hypothesis.objects.filter(category='SCI')]
    hypothesis2 = [x.text for x in Hypothesis.objects.filter(category='P')]
    sci_overview = get_overview("SCI")
    # For probability
    probability_overview = get_overview('P')
    return render(request, 'overview.html', {'sci_overview': sci_overview, 'hint1': hypothesis1, 'hint2':hypothesis2, 'p_overview': probability_overview})

@login_required(login_url='/risk_evidence/login')
def visual_map(request):
    sci_overview = get_overview("SCI")
    probability_overview = get_overview('P')
    brief = Hypothesis.objects.filter(category="SCI").values("brief").order_by('num')

    hypothesis_brief = {}
    for i in range(23):
        hypothesis_brief['h%d' % (i+1)] = brief[i]

    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]

    footwear_workers_by_country, footwear_workers_total = get_workers_num('FOOTWEAR')
    apparel_workers_by_country, apparel_workers_total = get_workers_num('APPAREL')

    data = []
    footwear_data = []
    apparel_data = []
    for country in country_list:
        v = []
        f_v = []
        a_v = []
        no_overlap = {}
        for x in range(23):
            h = 'h%d' % (x+1)
            if probability_overview[country][x] > 0.01 and sci_overview[country][x] >= 0:
                if footwear_workers_by_country[country] > 0 and request.method == 'POST' and 'btn2' in request.POST:
                    f_v.append({"y": probability_overview[country][x],
                                "x": sci_overview[country][x] * footwear_workers_by_country[country] / footwear_workers_total,
                                "shape": "circle", "size": random.random(), 'tooltip': h + ' - ' + hypothesis_brief[h]['brief']})
                elif request.method == 'POST' and 'btn3' in request.POST:
                    a_v.append({"y": probability_overview[country][x],
                                "x": sci_overview[country][x] * apparel_workers_by_country[country] / apparel_workers_total,
                                "shape": "circle", "size": random.random(), 'tooltip': h + ' - ' + hypothesis_brief[h]['brief']})
                else:
                    if (probability_overview[country][x], sci_overview[country][x]) not in no_overlap.keys():
                        no_overlap[(probability_overview[country][x], sci_overview[country][x])] = [h + ' - ' + hypothesis_brief[h]['brief']]
                    else:
                        no_overlap[(probability_overview[country][x], sci_overview[country][x])].append(h + ' - ' + hypothesis_brief[h]['brief'])

        if request.method == 'POST' and 'btn2' in request.POST:
            footwear_data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': f_v,
                        'slope': 0.000000001,
                        'intercept': .5,
                    }
            )

        elif request.method == 'POST' and 'btn3' in request.POST:
            apparel_data.append({
                        'yAxis': 1,
                        'key': country,
                        'values': a_v,
                        'slope': 0.000000001,
                        'intercept': .5,
                    })

        else:
            for key, value in no_overlap.iteritems():
                v.append({"y": key[0], "x": key[1], "shape": "circle", "size": random.random(), 'tooltip': ','.join(value)})

            data.append({
                            'yAxis': 1,
                            'key': country,
                            'values': v,
                            'slope': 0.000000001,
                            'intercept': .5,
            })

    if request.method == 'POST':
        if 'btn1' in request.POST:
            return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(data), 'type': 'Overall'})
        elif 'btn2' in request.POST:
            return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(footwear_data), 'type': 'Footwear'})
        elif 'btn3' in request.POST:
            return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(apparel_data), 'type': 'Apparel'})

    return render(request, 'visual_map.html', {'data_scatterchart_container': json.dumps(data), 'type': 'Overall'})


@login_required(login_url='/risk_evidence/login')
def visual_map_original(request):
    sci_overview = get_overview("SCI", original=True)
    probability_overview = get_overview('P', original=True)
    brief = Hypothesis.objects.filter(category="SCI").values("brief").order_by('num')

    hypothesis_brief = {}
    for i in range(23):
        hypothesis_brief['h%d' % (i+1)] = brief[i]

    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]

    footwear_workers_by_country, footwear_workers_total = get_workers_num('FOOTWEAR')
    apparel_workers_by_country, apparel_workers_total = get_workers_num('APPAREL')

    data = []
    footwear_data = []
    apparel_data = []
    for country in country_list:
        v = []
        f_v = []
        a_v = []
        no_overlap = {}
        for x in range(23):
            h = 'h%d' % (x+1)
            if probability_overview[country][x] > 0 and sci_overview[country][x] >= 0:
                if footwear_workers_by_country[country] > 0 and request.method == 'POST' and 'btn2' in request.POST:
                    f_v.append({"y": probability_overview[country][x],
                                "x": sci_overview[country][x] * footwear_workers_by_country[country] / footwear_workers_total,
                                "shape": "circle", "size": random.random(), 'tooltip': h + ' - ' + hypothesis_brief[h]['brief']})
                elif request.method == 'POST' and 'btn3' in request.POST:
                    a_v.append({"y": probability_overview[country][x],
                                "x": sci_overview[country][x] * apparel_workers_by_country[country] / apparel_workers_total,
                                "shape": "circle", "size": random.random(), 'tooltip': h + ' - ' + hypothesis_brief[h]['brief']})
                else:
                    if (probability_overview[country][x], sci_overview[country][x]) not in no_overlap.keys():
                        no_overlap[(probability_overview[country][x], sci_overview[country][x])] = [h + ' - ' + hypothesis_brief[h]['brief']]
                    else:
                        no_overlap[(probability_overview[country][x], sci_overview[country][x])].append(h + ' - ' + hypothesis_brief[h]['brief'])

        if request.method == 'POST' and 'btn2' in request.POST:
            footwear_data.append(
                    {
                        'yAxis': 1,
                        'key': country,
                        'values': f_v,
                        'slope': 0.000000001,
                        'intercept': .5,
                    }
            )

        elif request.method == 'POST' and 'btn3' in request.POST:
            apparel_data.append({
                        'yAxis': 1,
                        'key': country,
                        'values': a_v,
                        'slope': 0.000000001,
                        'intercept': .5,
                    })

        else:
            for key, value in no_overlap.iteritems():
                v.append({"y": key[0], "x": key[1], "shape": "circle", "size": random.random(), 'tooltip': ','.join(value)})

            data.append({
                            'yAxis': 1,
                            'key': country,
                            'values': v,
                            'slope': 0.000000001,
                            'intercept': .5,
            })

    if request.method == 'POST':
        if 'btn1' in request.POST:
            return render(request, 'visual_map_original.html', {'data_scatterchart_container_2': json.dumps(data), 'type': 'Overall'})
        elif 'btn2' in request.POST:
            return render(request, 'visual_map_original.html', {'data_scatterchart_container_2': json.dumps(footwear_data), 'type': 'Footwear'})
        elif 'btn3' in request.POST:
            return render(request, 'visual_map_original.html', {'data_scatterchart_container_2': json.dumps(apparel_data), 'type': 'Apparel'})

    return render(request, 'visual_map_original.html', {'data_scatterchart_container_2': json.dumps(data), 'type': 'Overall'})



@login_required(login_url='/risk_evidence/login')
def hypothesis_list(request):
    sci = [(x.num, x.area, x.text) for x in Hypothesis.objects.filter(category="SCI")]

    sci_area = [(sci[0][1].strip(), [])]
    for h in sci:
        if h[1].strip() == sci_area[-1][0]:
            sci_area[-1][1].append((h[0], h[2]))
        else:
            sci_area.append(
                (h[1], [(h[0], h[2])])
            )

    p = [(x.num, x.area, x.text) for x in Hypothesis.objects.filter(category="P")]

    p_area = [(p[0][1].strip(), [])]
    for h in p:
        if h[1].strip() == p_area[-1][0]:
            p_area[-1][1].append((h[0], h[2]))
        else:
            p_area.append(
                (h[1], [(h[0], h[2])])
            )
    return render(request, 'hypothesis_list.html', {'sci': sci_area, 'p': p_area})

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
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rlogin.html', {})

@login_required(login_url='/risk_evidence/login')
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

