from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import OMANG, FEMALE, MALE
from edc_facility.import_holidays import import_holidays
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


@tag('sc')
class TestRuleGroups(TestCase):

    def setUp(self):
        import_holidays()

        self.eligibility = mommy.make_recipe(
            'training_subject.eligibilityconfirmation')

        self.consent_options = {
            'screening_identifier': self.eligibility.screening_identifier,
            'consent_datetime': get_utcnow(),
            'version': 1,
            'dob': (get_utcnow() - relativedelta(years=45)).date(),
            'first_name': 'TEST ONE',
            'last_name': 'TEST',
            'initials': 'TOT',
            'identity': '123425678',
            'confirm_identity': '123425678',
            'identity_type': OMANG,
            'gender': FEMALE}

        self.subject_consent = mommy.make_recipe(
            'training_subject.informedconsent',
            **self.consent_options)

        self.subject_identifier = self.subject_consent.subject_identifier

        mommy.make_recipe(
            'training_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1000'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

    def test_pregnancy_form_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='training_subject.pregnancytest',
                subject_identifier=self.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, REQUIRED)

    def test_pregnancy_form_not_required(self):

        eligibility = mommy.make_recipe(
            'training_subject.eligibilityconfirmation')

        consent_options = {
            'screening_identifier': eligibility.screening_identifier,
            'consent_datetime': get_utcnow(),
            'version': 1,
            'dob': (get_utcnow() - relativedelta(years=45)).date(),
            'first_name': 'JOHN',
            'last_name': 'DOE',
            'initials': 'JD',
            'identity': '123415678',
            'confirm_identity': '123415678',
            'identity_type': OMANG,
            'gender': MALE}

        subject_consent = mommy.make_recipe(
            'training_subject.informedconsent',
            **consent_options)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='training_subject.pregnancytest',
                subject_identifier=subject_consent.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, NOT_REQUIRED)
