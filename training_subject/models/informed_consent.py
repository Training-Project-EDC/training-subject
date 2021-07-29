from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import PersonalFieldsMixin, VulnerabilityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.validators import eligible_if_yes
from edc_constants.choices import YES_NO
from ..choices import RELATIONSHIP_STATUS, CURRENTLY_LIVE_WITH

from ..choices import IDENTITY_TYPE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager

from .model_mixins import SearchSlugModelMixin
from ..choices import GENDER_OTHER
from ..subject_identifier import SubjectIdentifier


class InformedConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class InformedConsent(ConsentModelMixin, SiteModelMixin,
                      UpdatesOrCreatesRegistrationModelMixin,
                      NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
                      PersonalFieldsMixin, VulnerabilityFieldsMixin,
                      SearchSlugModelMixin, BaseUuidModel):
    subject_screening_model = 'training_subject.eligibilityconfirmation'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        max_length=50)

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        default=get_utcnow,
        help_text='Date and time of consent.')

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=30,
        choices=IDENTITY_TYPE)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER_OTHER,
        max_length=5,
        null=True,
        blank=False)

    marital_status = models.CharField(
        choices=RELATIONSHIP_STATUS,
        max_length=10,
    )

    women_question = models.PositiveSmallIntegerField(
        verbose_name='How many wives does your husband have?',
    )

    man_question = models.PositiveSmallIntegerField(
        verbose_name='How wives do you have?',
    )

    dwelling_with = models.CharField(
        verbose_name='Who do you currently live with?',
        max_length=20,
        choices=CURRENTLY_LIVE_WITH
    )


    is_eligible = models.BooleanField(default=True)

    objects = InformedConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def natural_key(self):
        return self.subject_identifier, self.version

    def save(self, *args, **kwargs):
        self.version = '1'
        super().save(*args, **kwargs)

    def make_new_identifier(self):
        """Returns a new and unique identifier.

        Override this if needed.
        """
        subject_identifier = SubjectIdentifier(
            identifier_type='subject',
            requesting_model=self._meta.label_lower,
            site=self.site)
        return subject_identifier.identifier

    @property
    def consent_version(self):
        return self.version

    class Meta(ConsentModelMixin.Meta):
        app_label = 'training_subject'
        verbose_name = 'Informed Consent'
        # unique_together = (
        #     ('subject_identifier', 'version'),
        #     ('subject_identifier', 'screening_identifier', 'version'),
        #     ('first_name', 'dob', 'initials', 'version'))
