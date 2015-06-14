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
        ('Relevance', 'Relevance',)
    ))

    def get_absolute_url(self):
        return reverse('score_edit', kwargs={'pk': self.pk})

class Country(models.Model):
    COUNTRY_CHOICES = (
        ('ARGENTINA', 'ARGENTINA'),
        ('AUSTRALIA', 'AUSTRALIA'),
        ('BANGLADESH', 'BANGLADESH'),
        ('BOSNIA', 'BOSNIA'),
        ('BRAZIL', 'BRAZIL'),
        ('BULGARIA', 'BULGARIA'),
        ('CAMBODIA', 'CAMBODIA'),
        ('CANADA', 'CANADA'),
        ('CHINA', 'CHINA'),
        ('ECUADOR', 'ECUADOR'),
        ('EGYPT', 'EGYPT'),
        ('EL SALVADOR', 'EL SALVADOR'),
        ('GEORGIA', 'GEORGIA'),
        ('GUATEMALA', 'GUATEMALA'),
        ('HONDURAS', 'HONDURAS'),
        ('HONG KONG (CHINA)', 'HONG KONG (CHINA)'),
        ('INDIA', 'INDIA'),
        ('INDONESIA', 'INDONESIA'),
        ('ISRAEL', 'ISRAEL'),
        ('ITALY', 'ITALY'),
        ('JAPAN', 'JAPAN'),
        ('JORDAN', 'JORDAN'),
        ('MACAU (CHINA)', 'MACAU (CHINA)'),
        ('MALAYSIA', 'MALAYSIA'),
        ('MEXICO', 'MEXICO'),
        ('MOLDOVA', 'MOLDOVA'),
        ('NETHERLANDS', 'NETHERLANDS'),
        ('NICARAGUA', 'NICARAGUA'),
        ('PAKISTAN', 'PAKISTAN'),
        ('PARAGUAY', 'PARAGUAY'),
        ('PERU', 'PERU'),
        ('PHILIPPINES', 'PHILIPPINES'),
        ('POLAND', 'POLAND'),
        ('PORTUGAL', 'PORTUGAL'),
        ('SOUTH AFRICA', 'SOUTH AFRICA'),
        ('SOUTH KOREA', 'SOUTH KOREA'),
        ('SPAIN', 'SPAIN'),
        ('SRI LANKA', 'SRI LANKA'),
        ('TAIWAN', 'TAIWAN'),
        ('THAILAND', 'THAILAND'),
        ('TURKEY', 'TURKEY'),
        ('UNITED KINGDOM', 'UNITED KINGDOM'),
        ('USA', 'USA'),
        ('VIETNAM', 'VIETNAM'),
    )
    name = models.CharField(unique=True, max_length=50, choices=COUNTRY_CHOICES)
    def __str__(self):
        return self.name


class Evidence(models.Model):
    evidence = models.TextField(default='')
    summary = models.TextField(default='')
    source = models.TextField(default='')
    country = models.ForeignKey(Country, to_field='name', default=None)
    type = models.CharField(max_length=30)
    CATEGORY_CHOICES = (
        ('SCI', 'Supply Chain Impact'),
        ('P', 'Probability'),
    )
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    LETTER_CHOICES = (
        ('I I', 'I I'),
        ('I', 'I'),
        ('NA', 'NA'),
        ('N', 'N'),
        ('C', 'C'),
        ('C C', 'C C'),
    )
    RATE_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    credibility = models.CharField(max_length=10, choices=RATE_CHOICES)
    relevance = models.CharField(max_length=10, choices=RATE_CHOICES)
    h1 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h2 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h3 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h4 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h5 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h6 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h7 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h8 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h9 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h10 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h11 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h12 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h13 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h14 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h15 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h16 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h17 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h18 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h19 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h20 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h21 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h22 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')
    h23 = models.CharField(max_length=5, choices=LETTER_CHOICES, default='NA')


class Hypothesis(models.Model):
    text = models.TextField(default='')
    # name = models.CharField(max_length=5,default='')
    num = models.IntegerField(default=0)
    CATEGORY_CHOICES = (
        ('SCI', 'Supply Chain Impact'),
        ('P', 'Probability'),
    )
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ('num',)
        unique_together = ('num', 'category')
