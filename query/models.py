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