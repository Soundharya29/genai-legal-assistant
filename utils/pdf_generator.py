from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_pdf_report(
    file_path,
    contract_type,
    overall_risk,
    summary,
    clauses,
    clause_risks
):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "GenAI Legal Assistant — Contract Risk Report")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 25

    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, f"Contract Type: {contract_type}")
    y -= 20

    c.drawString(40, y, f"Overall Contract Risk: {overall_risk}")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Plain-English Summary")
    y -= 20

    c.setFont("Helvetica", 10)
    for line in summary.split(". "):
        c.drawString(40, y, line.strip())
        y -= 14

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Clause Risk Breakdown")
    y -= 20

    c.setFont("Helvetica", 10)
    for i, (clause, risk) in enumerate(zip(clauses, clause_risks), start=1):
        if y < 80:
            c.showPage()
            y = height - 40
            c.setFont("Helvetica", 10)

        c.drawString(40, y, f"Clause {i}: {risk}")
        y -= 14

    c.save()
