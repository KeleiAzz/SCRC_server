from models import Score, Evidence


def get_num_scales(category):
    credibility = {
    'High': Score.objects.get(letter_scale='High', category=category, sub_category='Credibility').num_scale,
    'Medium': Score.objects.get(letter_scale='Medium', category=category, sub_category='Credibility').num_scale,
    'Low': Score.objects.get(letter_scale='Low', category=category, sub_category='Credibility').num_scale}

    relevance = {'High': Score.objects.get(letter_scale='High', category=category, sub_category='Relevance').num_scale,
                 'Medium': Score.objects.get(letter_scale='Medium', category=category,
                                             sub_category='Relevance').num_scale,
                 'Low': Score.objects.get(letter_scale='Low', category=category, sub_category='Relevance').num_scale}

    letter_scale = {'I I': Score.objects.get(letter_scale='I I', category=category).num_scale,
                    'I': Score.objects.get(letter_scale='I', category=category).num_scale,
                    'NA': Score.objects.get(letter_scale='NA', category=category).num_scale,
                    'N': Score.objects.get(letter_scale='N', category=category).num_scale,
                    'C': Score.objects.get(letter_scale='C', category=category).num_scale,
                    'C C': Score.objects.get(letter_scale='C C', category=category).num_scale}

    return credibility, relevance, letter_scale

def get_overview(category):
    country_list = [x[0] for x in Evidence.objects.values_list('country').distinct()]
    hypothesis = []
    overview = {}

    for i in range(1, 24, 1):
        hypothesis.append('h' + str(i))

    if category == "SCI":
        credibility, relevance, letter_scale = get_num_scales(category)
        overview = {}
        for country in country_list:
            overview[country] = []
            for h in hypothesis:
                evidences = Evidence.objects.filter(country_id=country, category=category)
                score = 0
                for e in evidences:
                    if getattr(e, h) == 'NA':
                        pass
                    else:
                        score += letter_scale[getattr(e, h)] * credibility[e.credibility] * relevance[e.relevance]
                overview[country].append(round(score, 3))
    else:
        credibility, relevance, letter_scale = get_num_scales('P')
        evidences_count = {}
        for country in country_list:
            overview[country] = []
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
                overview[country].append(score)
                if evidences_count[country][-1] == 0:
                    evidences_count[country][-1] = 1

            for i in range(len(overview[country])):
                overview[country][i] = round(overview[country][i]/(evidences_count[country][i] * credibility['High'] * relevance['High'] * letter_scale['C C']), 3)
    return overview
