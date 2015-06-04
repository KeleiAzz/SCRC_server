from django import forms
from risk_evidence.models import Score
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