import streamlit as st

from nlp.entity_extractor import extract_medical_entities
from nlp.medical_mapper import simplify_terms
from models.medical_llm import simplify_report
from utils.risk_detector import detect_risk
from utils.pdf_reader import extract_text_from_pdf
from utils.pdf_generator import create_pdf

st.title("🩺 AI Medical Report Simplifier")

st.write("Convert complex medical reports into simple patient-friendly explanations.")

report = ""

uploaded_file = st.file_uploader("Upload Medical Report (PDF)", type=["pdf"])

if uploaded_file:
    report = extract_text_from_pdf(uploaded_file)

report_text = st.text_area("Or Paste Medical Report")

if report_text.strip():
    report = report_text

if st.button("Simplify Report"):

    if report.strip() == "":
        st.warning("Please upload or paste a medical report.")

    else:

        entities = extract_medical_entities(report)

        simplified_terms = simplify_terms(report)

        explanation = simplify_report(simplified_terms)

        
        risk = detect_risk(report + explanation)

        st.subheader("🧾 Simplified Explanation")
        st.success(explanation)

        st.subheader("🔬 Detected Medical Terms")

        for e in entities:
            st.write("•", e)

        st.subheader("⚠ Risk Assessment")
        st.warning(risk)

        pdf = create_pdf(explanation)

        st.download_button(
            label="Download Simplified Report PDF",
            data=pdf,
            file_name="simplified_report.pdf",
            mime="application/pdf"
        )