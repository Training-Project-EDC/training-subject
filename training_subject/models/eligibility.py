from edc_constants.constants import YES
# from .eligibility_confirmation import EligibilityConfirmation

AGE_THRESH_HOLD = 18


class Eligibility:

    def __init__(self, subject):
        self.error_message = []
        self._subject = subject

    def is_eligible(self):
        return self._check_age() and self._check_literate() and self._check_nationality()

    def _check_age(self):
        result = False
        if self._subject.age < AGE_THRESH_HOLD and self._subject.is_guardian_avaliable == YES:
            result = True
        elif self._subject.age >= AGE_THRESH_HOLD:
            result = True
        else:
            self.error_message.append('Age not permitted for consent')
            result = False
        return result

    def _check_nationality(self):
        result = False
        if self._subject.country_of_origin == 'BW':
            result = True
        elif self._subject.spouse_country_of_origin == 'BW':
            result = True
        else:
            self.error_message.append('Not eligible')
            return result
        return result

    def _check_literate(self):
        return self._subject.is_literate == YES

