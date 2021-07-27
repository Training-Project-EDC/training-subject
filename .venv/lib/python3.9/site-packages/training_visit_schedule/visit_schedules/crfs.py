from edc_visit_schedule import FormsCollection, Crf, Requisition

crf = {}

crf_initial = FormsCollection(
    Crf(show_order=10, model='training_subject.educationquestionnaire'),
    name='initial'
)

crf_second = FormsCollection(
    Crf(show_order=20, model='training_subject.communityquestionnaire'),
    name='followup'
)

# requisitions = FormsCollection(
#     Requisition(
#         show_order=10, model='training_subject.subjectrequisition', panel_name='Training Requisition Model'),
# )

crfs = {
    'initial': crf_initial,
    'followup': crf_second,
}
