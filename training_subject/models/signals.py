from django.apps import apps as django_apps
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_constants.constants import YES
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from django.core.exceptions import ValidationError
# from .covid19_symptomatic_infections import Covid19SymptomaticInfections
from .informed_consent import InformedConsent
from .onschedule import OnSchedule
from edc_visit_schedule.schedule import Schedule


@receiver(post_save, weak=False, sender=InformedConsent, dispatch_uid='informed_consent_on_post_save')
def informed_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """ Put participant on schedule post consent """
    if not raw:
        if created:
            pass
            # instance.registration_update_or_create()
            # update_model_fields(instance=instance,
            #                     model_cls=['subject_identifier', instance.subject_identifier])
        try:
            OnSchedule.objects.get(
                subject_identifier=instance.subject_identifier, )
        except OnSchedule.DoesNotExist:
            onschedule_model = 'training_subject.onschedule'
            put_on_schedule(schedule_name='training_subject_visit_schedule', instance=instance, onschedule_model=onschedule_model)


def put_on_schedule(schedule_name, onschedule_model, instance=None):
    if instance:

        _, schedule = site_visit_schedules.get_by_onschedule_model(
            onschedule_model=onschedule_model)

        onschedule_model_cls = django_apps.get_model(onschedule_model)

        try:
            onschedule_model_cls.objects.get(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)
        except onschedule_model_cls.DoesNotExist:
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.consent_datetime,
                schedule_name=schedule_name)
        else:
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)


def update_model_fields(instance=None, model_cls=None, fields=None):
    """
    Use to update a specific attribute for a particular model
    """
    try:
        model_obj = model_cls.objects.get(
            screening_identifier=instance.screening_identifier)
    except model_cls.DoesNotExist:
        raise ValidationError(f'{model_cls} object does not exist!')
    else:
        for field, value in fields:
            setattr(model_obj, field, value)
        model_obj.save_base(update_fields=[field[0] for field in fields])
