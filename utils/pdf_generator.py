from fpdf import FPDF

def create_pdf(explanation):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Simplified Medical Report", ln=True)

    pdf.ln(10)

    pdf.set_font("Arial", "", 12)

    # Write explanation text
    if explanation:
        pdf.multi_cell(0, 10, explanation)
    else:
        pdf.multi_cell(0, 10, "No explanation generated.")

    # Convert to bytes for Streamlit download
    pdf_bytes = pdf.output(dest="S").encode("latin-1")

    return pdf_bytes