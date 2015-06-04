from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from models import Score
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
    return render(request, 'score_list.html', {'scores': scores})