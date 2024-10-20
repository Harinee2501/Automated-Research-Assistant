from fpdf import FPDF

def generate_pdf(wikipedia_summary,webpage_content):
    pdf=FPDF()
    pdf.set_auto_page_break(auto=True,margin=15)
    pdf.add_page()

    pdf.set_font("Arial",'B',16)
    pdf.cell(0,10,'Research Summary',ln=True,align='C')
    pdf.set_font("Arial",'I',12)
    pdf.cell(0,10,'Wikipedia Summary:',ln=True)

    pdf.set_font("Arial",'',12)
    for line in wikipedia_summary.split('\n'):
        pdf.multi_cell(0,10,line)

    pdf.set_font("Arial",'I',12)
    pdf.cell(0,10,line)

    pdf_file_path="research_summary.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path