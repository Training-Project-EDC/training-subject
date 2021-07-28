from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..forms import SubjectLocatorForm
from ..models import PersonalContactInfo
from ..admin_site import training_subject_admin
from .modeladmin_mixins import ModelAdminMixin


@admin.register(PersonalContactInfo, site=training_subject_admin)
class SubjectLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
                'date_signed',
                'may_visit_home',
                'physical_address',
                'may_call',
                'subject_cell',
                'subject_cell_alt',
                'subject_phone',
                'subject_phone_alt',
                'may_call_work',
                'subject_work_place',
                'subject_work_phone',
                'may_contact_indirectly',
                'indirect_contact_name',
                'indirect_contact_relation',
                'indirect_contact_physical_address',
                'indirect_contact_cell',
                'indirect_contact_phone',
            ),
        }),
        audit_fieldset_tuple)

    radio_fields = {'may_visit_home': admin.VERTICAL,
                    'may_call': admin.VERTICAL,
                    'may_call_work': admin.VERTICAL,
                    'may_contact_indirectly': admin.VERTICAL, }

    search_fields = ('subject_identifier', )

    list_display = ('subject_identifier', 'may_visit_home', 'may_call',
                    'may_call_work')
