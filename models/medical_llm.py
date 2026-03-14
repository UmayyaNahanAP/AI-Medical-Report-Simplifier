def simplify_report(text):

    text_lower = text.lower()

    explanation = []

    # Detect possible heart attack
    if "myocardial infarction" in text_lower or "st elevation" in text_lower:
        explanation.append(
            "The test results suggest that the patient may be having a heart attack."
        )

    if "chest pain" in text_lower:
        explanation.append(
            "The patient is experiencing severe chest pain that spreads to the arm or jaw."
        )

    if "dyspnea" in text_lower or "shortness of breath" in text_lower:
        explanation.append(
            "The patient is having difficulty breathing."
        )

    if "tachycardia" in text_lower or "fast heart rate" in text_lower:
        explanation.append(
            "The patient's heart rate is faster than normal."
        )

    if "hypertension" in text_lower or "high blood pressure" in text_lower:
        explanation.append(
            "The patient has high blood pressure, which increases heart risk."
        )

    # Default message if nothing detected
    if not explanation:
        explanation.append(
            "The medical report indicates some health concerns that should be evaluated by a doctor."
        )

    explanation.append(
        "Immediate medical attention and proper evaluation by a healthcare professional is recommended."
    )

    return " ".join(explanation)