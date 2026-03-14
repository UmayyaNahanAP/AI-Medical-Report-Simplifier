def detect_risk(text):

    critical_terms = [
        "heart attack",
        "myocardial infarction",
        "stroke",
        "cardiac arrest",
        "severe chest pain",
    ]

    text = text.lower()

    for term in critical_terms:
        if term in text:
            return "⚠ Serious condition detected. Immediate medical attention recommended."

    return "No critical risk detected."