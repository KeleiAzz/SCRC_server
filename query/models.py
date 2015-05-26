from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=20)
    bloomberg_ticker = models.CharField(max_length=20)
    website = models.TextField(default='')
    industry_group = models.CharField(max_length=100)
    industry_subgroup = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Rating(models.Model):
    company = models.ForeignKey(Company)
    category = models.ForeignKey(Category)
    date = models.DateField(default=None)
    score = models.FloatField(default=0)
    expire_date = models.DateField(default=None)

class Evidence(models.Model):
    name = models.TextField(default='')
    note = models.TextField(default='')
    link = models.TextField(default='')
    country = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    credibility = models.CharField(max_length=30)
    relevance = models.CharField(max_length=30)
    h1 = models.IntegerField(blank=True, null=True)
    h2 = models.IntegerField(blank=True, null=True)
    h3 = models.IntegerField(blank=True, null=True)
    h4 = models.IntegerField(blank=True, null=True)
    h5 = models.IntegerField(blank=True, null=True)
    h6 = models.IntegerField(blank=True, null=True)
    h7 = models.IntegerField(blank=True, null=True)
    h8 = models.IntegerField(blank=True, null=True)
    h9 = models.IntegerField(blank=True, null=True)
    h10 = models.IntegerField(blank=True, null=True)
    h11 = models.IntegerField(blank=True, null=True)
    h12 = models.IntegerField(blank=True, null=True)
    h13 = models.IntegerField(blank=True, null=True)
    h14 = models.IntegerField(blank=True, null=True)
    h15 = models.IntegerField(blank=True, null=True)
    h16 = models.IntegerField(blank=True, null=True)
    h17 = models.IntegerField(blank=True, null=True)
    h18 = models.IntegerField(blank=True, null=True)
    h19 = models.IntegerField(blank=True, null=True)
    h20 = models.IntegerField(blank=True, null=True)
    h21 = models.IntegerField(blank=True, null=True)
    h22 = models.IntegerField(blank=True, null=True)
    h23 = models.IntegerField(blank=True, null=True)

