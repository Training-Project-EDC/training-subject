from django import forms
from django.core.exceptions import ValidationError
from edc_constants.constants import OTHER
from edc_form_validators import FormValidatorMixin

from ..models import EducationQuestionnaire


class EducationQuestionnaireForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = EducationQuestionnaire
        fields = '__all__'

    # def clean_other_type_of_work(self):
    #     data = self.cleaned_data['type_of_work']
    #     if data == OTHER:
    #         raise ValidationError('Please specify')
    #     else:
    #         raise ValidationError('Please specify')
    #     return data
