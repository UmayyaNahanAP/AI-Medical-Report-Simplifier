import spacy

nlp = spacy.load("en_core_web_sm")

medical_keywords = [
    "myocardial infarction",
    "hypertension",
    "tachycardia",
    "dyspnea",
    "troponin",
    "ecg",
    "electrocardiogram",
]

def extract_medical_entities(text):

    text_lower = text.lower()

    entities = []

    for term in medical_keywords:
        if term in text_lower:
            entities.append(term)

    return list(set(entities))