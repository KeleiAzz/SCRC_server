from django import forms
from query.models import Company, Rating, Evidence



class MultipleChoiceForm(forms.Form):
    class Meta:
        model = Company
        # field = ('id', 'name',)
    def __init__(self, request, *args, **kwargs):
        super(MultipleChoiceForm, self).__init__(*args, **kwargs)
        if request.POST.get('company_name', 0) != 0:
            Company_CHOICES = [[x.id, x.name] for x in Company.objects.all().filter(name__icontains=request.POST['company_name'])]
        else:
            Company_CHOICES = [[x.id, x.name] for x in Company.objects.all()]

        self.fields['choice_field'] = forms.MultipleChoiceField(choices=Company_CHOICES, widget=forms.SelectMultiple())

class CountryChoiceForm(forms.Form):
    # class Meta:
    #     model = Evidence
        # field = ('id', 'name',)
    def __init__(self, *args, **kwargs):
        super(CountryChoiceForm, self).__init__(*args, **kwargs)
        country_choices = [[1, x[0]] for x in Evidence.objects.values_list('country').distinct()]
        # country_choices = list(set(country_choices))
        # country_choices = ['a', 'b', 'c']
        self.fields[' '] = forms.MultipleChoiceField(choices=country_choices, widget=forms.SelectMultiple())
