from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from models import Score, Evidence
from forms import ScoreForm, CountryChoiceForm, EvidenceForm
# Create your views here.


# class ScoreCreate(UpdateView):
#     model = Score
#     fields = ['letter_scale']

def score_create(request):
    form = Score
    return render(request, 'score_create_form.html', {'form': form})

def home(request):
    return render(request, 'dashboard.html')

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
        country_form = CountryChoiceForm
        return render(request, 'evidence_list.html', {'evidences': evidences, 'hint': hint, 'country': country, 'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'evidence_list.html', {
            # 'evidences': evidences,
            'hint': hint,
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
        country_form = CountryChoiceForm
        return render(request, 'probability_list.html', {'evidences': evidences, 'hint': hint, 'country': country,
                                                         'country_form': country_form})
    else:
        country_form = CountryChoiceForm
        return render(request, 'probability_list.html', { 'hint': hint,'country_form': country_form})

def evidence_add(request):
    if request.method == 'POST':
        form = EvidenceForm(request.POST)
        form.save()
        if request.POST.get('category') == 'SCI':
            return redirect('sci_list')
        else:
            return redirect('probability_list')
    form = EvidenceForm()
    return render(request, 'evidence_add.html', {'form': form})