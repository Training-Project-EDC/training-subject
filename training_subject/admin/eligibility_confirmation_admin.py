from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin
from ..forms import EligibilityConfirmationForm
from ..models import EligibilityConfirmation
from ..admin_site import training_subject_admin


@admin.register(EligibilityConfirmation, site=training_subject_admin)
class EligibilityConfirmationAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = EligibilityConfirmationForm
    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'report_datetime',
                'gender',
                'age',
                'country_of_origin',
                'is_married',
                'spouse_country_of_origin',
                'is_literate')}),
        audit_fieldset_tuple)

    radio_fields = {
        'gender': admin.VERTICAL,
        'is_married': admin.VERTICAL,
        'is_literate': admin.VERTICAL, }

    search_fields = ['screening_identifier']

    readonly_fields = ('screening_identifier',)
