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