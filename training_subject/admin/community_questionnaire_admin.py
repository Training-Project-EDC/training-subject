from django.contrib import admin
from edc_model_admin import ModelAdminBasicMixin
from simple_history.admin import SimpleHistoryAdmin

from training_subject.admin.modeladmin_mixins import CrfModelAdminMixin
from training_subject.admin_site import training_subject_admin
from training_subject.forms import CommunityQuestionnaireForm
from training_subject.models import CommunityQuestionnaire


@admin.register(CommunityQuestionnaire, site=training_subject_admin)
class CommunityQuestionnaireAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = CommunityQuestionnaireForm

    radio_fields = {
        'active_community': admin.VERTICAL,
        'did_you_vote': admin.VERTICAL,
        'problem_in_neighborhood': admin.VERTICAL
    }

    filter_horizontal = ('neighborhood',)
