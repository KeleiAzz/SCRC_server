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

