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


class Evidence(models.Model):
    name = models.TextField(default='')
    note = models.TextField(default='')
    link = models.TextField(default='')
    country = models.ForeignKey(Country)
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
    h1 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h2 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h3 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h4 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h5 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h6 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h7 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h8 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h9 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h10 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h11 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h12 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h13 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h14 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h15 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h16 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h17 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h18 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h19 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h20 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h21 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h22 = models.CharField(max_length=5, choices=LETTER_CHOICES)
    h23 = models.CharField(max_length=5, choices=LETTER_CHOICES)


