from fpdf import FPDF

def generate_pdf(topic, summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Topic: {topic}\n\nSummary:\n{summary}")
    pdf.output("paper_output.pdf")
