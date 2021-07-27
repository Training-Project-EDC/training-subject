from django.contrib import admin

from ..admin_site import training_subject_admin
from ..models import EducationQuestionnaire
from ..forms import EducationQuestionnaireForm


@admin.register(EducationQuestionnaire, site=training_subject_admin)
class EducationQuestionnaireAdmin(admin.ModelAdmin):
    form = EducationQuestionnaireForm
