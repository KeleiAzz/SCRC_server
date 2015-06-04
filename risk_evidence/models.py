from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Score(models.Model):
    LETTER_CHOICES = (
        ('I I', 'I I'),
        ('I', 'I'),
        ('NA', 'NA'),
        ('N', 'N'),
        ('C', 'C'),
        ('C C', 'C C'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    letter_scale = models.CharField(max_length=10, choices=LETTER_CHOICES)
    num_scale = models.FloatField(blank=True, null=True)
    CATEGORY_CHOICES = (
        ('SCI', 'Supply Chain Impact'),
        ('P', 'Probability'),
    )
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    definition = models.TextField(default='')
    sub_category = models.CharField(max_length=15, blank=True, null=True, choices=(
        ('Credibility', 'Credibility'),
        ('Revelance', 'Revelance',)
    ))

    def get_absolute_url(self):
        return reverse('score_edit', kwargs={'pk': self.pk})



class Evidence(models.Model):
    name = models.TextField(default='')
    note = models.TextField(default='')
    link = models.TextField(default='')
    country = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    CATEGORY_CHOICES = (
        ('SCI', 'Supply Chain Impact'),
        ('P', 'Probability'),
    )
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    credibility = models.ForeignKey(Score, limit_choices_to={'sub_category': 'Credibility'}, related_name='+')
    revelance = models.ForeignKey(Score, limit_choices_to={'sub_category': 'Revelance'}, related_name='+')
    h1 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h2 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h3 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h4 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h5 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h6 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h7 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h8 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h9 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h10 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h11 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h12 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h13 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h14 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h15 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h16 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h17 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h18 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h19 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h20 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h21 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h22 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
    h23 = models.ForeignKey(Score, limit_choices_to={'sub_category': None}, related_name='+')
