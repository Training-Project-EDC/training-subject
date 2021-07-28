from django.test import TestCase, tag

from ..models.eligibility import Eligibility
from ..models.eligibility_confirmation import EligibilityConfirmation
from edc_constants.constants import YES


class EligibilityTests(TestCase):

    def test_valid_participant_age_eligibility(self):
        eligibility = EligibilityConfirmation()
        eligibility.age = 23
        self.assertTrue(Eligibility(eligibility)._check_age())

    def test_subject_citizenship_valid(self):
        eligibility = EligibilityConfirmation()
        eligibility.country_of_origin = 'BW'
        self.assertTrue(Eligibility(eligibility)._check_nationality())

    def test_subject_non_citizenship_valid(self):
        eligibility = EligibilityConfirmation()
        eligibility.country_of_origin = 'ZW'
        eligibility.spouse_country_of_origin = 'BW'
        self.assertTrue(Eligibility(eligibility)._check_nationality())

    def test_subject_literate_valid(self):
        eligibility = EligibilityConfirmation()
        eligibility.is_literate = YES
        self.assertTrue(Eligibility(eligibility)._check_literate())
