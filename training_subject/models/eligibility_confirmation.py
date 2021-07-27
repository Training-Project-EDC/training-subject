from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugManager
from edc_constants.choices import YES_NO, GENDER
from ..choices import COUNTRIES

from .eligibility import Eligibility
from .model_mixins import SearchSlugModelMixin
from ..identifiers import ScreeningIdentifier


class EligibilityConfirmationManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class EligibilityConfirmation(NonUniqueSubjectIdentifierFieldMixin,
                              SiteModelMixin,
                              SearchSlugModelMixin, BaseUuidModel):
    identifier_cls = ScreeningIdentifier

    screening_identifier = models.CharField(
        verbose_name='Eligibility Identifier',
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text='Date and time of report.')

    gender = models.CharField(
        choices=GENDER,
        verbose_name='Gender',
        max_length=10,
        help_text='Male or Female', )

    age = models.PositiveSmallIntegerField(
        verbose_name='Age',
        help_text='How old is the subject? ', )

    country_of_origin = models.CharField(
        verbose_name="Subject country of origin",
        default="BW",
        max_length=5,
        choices=COUNTRIES
    )

    is_married = models.CharField(
        verbose_name='Is the subject married?',
        max_length=10,
        choices=YES_NO,
        help_text='If yes, the a marriage certificate should be produced')

    spouse_country_of_origin = models.CharField(
        verbose_name="Subject spouse country of origin if married?",
        default="BW",
        max_length=5,
        choices=COUNTRIES)

    is_literate = models.CharField(
        verbose_name="Is the subject literate?",
        max_length=5,
        choices=YES_NO)

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    # is updated via signal once subject is consented
    is_consented = models.BooleanField(
        default=False,
        editable=False)

    history = HistoricalRecords()

    objects = EligibilityConfirmationManager()

    def __str__(self):
        return self.screening_identifier

    def natural_key(self):
        return self.screening_identifier

    def save(self, *args, **kwargs):
        eligibility_criteria = Eligibility(self)
        self.is_eligible = eligibility_criteria.is_eligible()
        self.ineligibility = eligibility_criteria.error_message
        if not self.screening_identifier:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('screening_identifier')
        return fields

    class Meta:
        app_label = 'training_subject'
        verbose_name = 'Eligibility Confirmation'
        verbose_name_plural = 'Eligibility Confirmation'
