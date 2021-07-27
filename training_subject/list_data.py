from edc_constants.constants import OTHER, NOT_APPLICABLE

from edc_list_data import PreloadData

list_data = {
    'training_subject.saecriteria': [
        ('death', 'Death'),
        ('life_threatening', 'Life-threatening'),
        ('hospitalization', 'Initial or prolonged hospitalization'),
        ('incapacity', 'Persistent or significant disability/incapacity'),
        ('birth_defects', 'Congenital anomaly/birth defect'),
        (OTHER, 'Other important medical event'),
    ],
    'training_subject.subjectrace': [
        ('american', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('african', 'Black or African American'),
        ('pacific_islander', 'Native Hawaiian or Other Pacific Islanders'),
        ('white', 'White'),
    ],
    'training_subject.covidsymptoms': [
        ('cough', 'Cough'),
        ('fever', 'Fever'),
        ('myalgia', 'Myalgia'),
        ('diarrhea', 'Diarrhea'),
        ('dyspnea', 'Dyspnea'),
        ('fatigue_or-Malaise', 'Fatigue or Malaise'),
        ('difficulty_in_breathing', 'Difficulty in breathing'),
        ('loss_of_smell', 'Loss of Smell'),
        ('loss_of_taste', 'Loss of Taste'),
        ('chills', 'Chills'),
        ('body_aches', 'Body aches'),
        ('headache', 'Headache'),
        ('sore_throat', 'Sore Throat'),
        ('vomiting', 'Vomiting'),
        ('congestion', 'Congestion'),
        ('runny_nose', 'Runny Nose'),
        ('nausea', 'Nausea'),
        ('hospitalization_outcome', 'Hospitalization Outcome'),
    ],
    'training_subject.contraception': [
        ('condoms', 'Condoms'),
        ('subdermal_implant', 'Subdermal implant'),
        ('injection', 'Injection'),
        ('intrauterine_device', 'Intrauterine Device'),
        ('diaphragm', 'Diaphragm'),
        ('contraceptive_pill', 'Contraceptive pill'),
        ('morning_after_pill', 'Morning after pill'),
        ('contraceptive_ring', 'Contraceptive ring'),
        ('contraceptive_implant', 'Contraceptive implant'),
        ('sterilization', 'Sterilization'),
        ('contraceptive_patch', 'Contraceptive patch'),
        ('abstinence', 'Abstinence'),
        ('tube_ligation', 'Tube ligation'),
        ('partner_vasectomy', 'Partner vasectomy'),
        (OTHER, 'Other, specify'),
    ],

    'training_subject.symptomaticinfections': [
        ('cough', 'Cough'),
        ('fever', 'Fever'),
        ('fatigue', 'Fatigue'),
        ('loss_of_smell', 'Loss of Smell'),
        ('loss_of_taste', 'Loss of Taste'),
        ('body_aches', 'Body aches'),
        ('headache', 'Headache'),
        ('shortness_of_breath', 'Shortness of breath'),
        ('muscle_aches', 'Muscle aches'),
        ('sore_throat', 'Sore throat'),
        ('chills', 'Chills'),
        ('congestion', 'Congestion'),
        ('runny_nose', 'Runny nose'),
        ('nausea', 'Nausea'),
        ('vomiting', 'Vomiting'),
        ('diarrhoea', 'Diarrhoea'),
        ('difficulty_breathing', 'Difficulty breathing')
    ],

    'training_subject.symptoms': [
        ('fever', 'Fever'),
        ('dry_cough', 'Dry Cough'),
        ('fatigue', 'Fatigue'),
        ('loss_of_taste_or_smell', 'Loss of taste or smell'),
        ('headache', 'Headache'),
        ('muscle_or_joint_pain', 'Muscle or joint pain'),
        ('shortness_of_breath', 'Shortness Of Breath'),
        ('difficulty_breathing_or_shortness_of_breath',
         'Difficulty breathing or shortness of breath'),
        ('chest_pain_or_pressure', 'Chest pain or pressure'),
        ('loss_of_speech_or_movement', 'Loss of speech or movement'),
        (OTHER, 'Other')
    ],
    'training_subject.diseases': [
        ('HIV', 'HIV'),
        ('malignancy', 'malignancy'),
        ('chronic_kidney_disease', 'Chronic Kidney Disease'),
        ('chronic_obstructive_pulmonary_disease', 'Chronic obstructive pulmonary disease'),
        ('other_chronic_lung_diseases', 'Other chronic lung diseases'),
        ('hypertension', 'Hypertension'),
        ('heart_failure', 'Heart failure'),
        ('coronary_artery_disease', 'Coronary artery disease'),
        ('cardiomyopathy', 'Cardiomyopathy'),
        ('pulmonary_hypertension', 'Pulmonary hypertension'),
        ('obesity', 'Obesity'),
        (OTHER, 'Other'),
        (NOT_APPLICABLE, 'Not Applicable')
    ]

}

preload_data = PreloadData(
    list_data=list_data)
