# AI Medical Report Simplifier

## Overview
The AI Medical Report Simplifier is an AI-powered healthcare assistant that converts complex medical reports into easy-to-understand explanations for patients.

Medical reports often contain technical terminology that can be difficult for patients to understand. This system processes clinical text and generates simplified explanations while highlighting important medical conditions.

## Features

- Upload medical report PDF
- Extract medical report text
- Detect medical entities
- Convert medical terminology to simple language
- Generate patient-friendly explanations
- Detect potential health risks
- Download simplified medical report as PDF

## Technologies Used

Python
Streamlit
spaCy
FPDF
PyMuPDF
HuggingFace (optional)

## System Architecture

Medical Report → Entity Extraction → Medical Term Mapping → Simplification Engine → Risk Detection → Streamlit Interface

## Installation

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

## Example

Input

Patient shows signs of myocardial infarction with elevated troponin levels.

Output

The patient may be experiencing a heart attack. Blood tests indicate possible damage to the heart muscle and immediate medical attention is recommended.

## Project Structure

app.py – Streamlit application  
entity_extractor.py – medical entity detection  
medical_mapper.py – term simplification  
medical_llm.py – explanation generation  
risk_detector.py – risk analysis  
pdf_reader.py – PDF extraction  
pdf_generator.py – PDF generation  

## Author

AI Healthcare Project