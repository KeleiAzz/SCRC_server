from django import forms
from risk_evidence.models import Score, Evidence
from django.core.exceptions import ValidationError

EMPTY_LIST_ERROR = "You can't have an empty list item"

class ScoreForm(forms.models.ModelForm):

    class Meta:
        model = Score
        fields = ('letter_scale', 'num_scale', 'definition', 'category', 'sub_category')
        # widgets = {
        #     'text': forms.fields.TextInput(attrs={
        #         'placeholder': 'Enter a to-do item',
        #         'class': 'form-control input-lg',
        #     }),
        # }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }
    # def save(self, for_list):
    #     self.instance.list = for_list
    #     return super().save()

    def save(self):
        return forms.models.ModelForm.save(self)

class CountryChoiceForm(forms.Form):
    # class Meta:
    #     model = Evidence
        # field = ('id', 'name',)
    def __init__(self, *args, **kwargs):
        super(CountryChoiceForm, self).__init__(*args, **kwargs)
        country_choices = [[x[0], x[0]] for x in Evidence.objects.values_list('country').distinct()]
        # country_choices = list(set(country_choices))
        # country_choices = ['a', 'b', 'c']
        self.fields['Select Country'] = forms.ChoiceField(choices=country_choices)


class EvidenceForm(forms.models.ModelForm):

    class Meta:
        model = Evidence
        fields = (
            'name',
            'note',
            'link',
            'type',
            'country',
            'category',
            'credibility',
            'relevance',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
            'h7',
            'h8',
            'h9',
            'h10',
            'h11',
            'h12',
            'h13',
            'h14',
            'h15',
            'h16',
            'h17',
            'h18',
            'h19',
            'h20',
            'h21',
            'h22',
            'h23',
        )
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'class': 'form-control2',
            }),
            'note': forms.fields.TextInput(attrs={
                'class': 'form-control2',
            }),
            'link': forms.fields.TextInput(attrs={
                'class': 'form-control2',
            }),
            'type': forms.fields.TextInput(attrs={
                'class': 'form-control2',
            }),
            'country': forms.fields.Select(attrs={
                'class': 'form-control3',
            }),
            'category': forms.fields.Select(attrs={
                'class': 'form-control3',
            }),
            'credibility': forms.fields.Select(attrs={
                'class': 'form-control3',
            }),
            'relevance': forms.fields.Select(attrs={
                'class': 'form-control3',
            }),
        }

    def save(self):
        return forms.models.ModelForm.save(self)