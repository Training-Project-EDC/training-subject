
from edc_constants.constants import YES

AGE_THRESH_HOLD = 18


class Eligibility:

    def __init__(self, subject):
        self.error_message = []
        pass

    def is_eligible(self):
        return True

    def __str__(self):
        # TODO: Return a readable string
        return ""
