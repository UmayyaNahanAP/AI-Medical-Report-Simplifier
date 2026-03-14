medical_dictionary = {

    "myocardial infarction": "heart attack",
    "hypertension": "high blood pressure",
    "dyspnea": "difficulty breathing",
    "tachycardia": "fast heart rate",
    "troponin": "heart damage indicator",
}

def simplify_terms(text):

    simplified = text

    for term, simple in medical_dictionary.items():

        simplified = simplified.replace(term, simple)

    return simplified