from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from models import Score
from forms import ScoreForm
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
    return render(request, 'score_list.html', {'scores': scores, 'form': ScoreForm})

def add_score(request):

    if request.method == 'POST':
        form = ScoreForm(request.POST)
        form.save()
        scores = Score.objects.all()
        return render(request, 'score_list.html', {'scores': scores})
    scores = Score.objects.all()
    return render(request, 'add_score.html', {'scores': scores, 'form': ScoreForm})

def edit_score(request, score_id):
    scores = Score.objects.all()
    instance = get_object_or_404(Score, id=score_id)
    form = ScoreForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('next_view')
    return render(request, 'edit_score.html', {'scores': scores,'form': form, "score_id": instance.id})
