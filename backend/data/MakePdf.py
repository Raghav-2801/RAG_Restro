from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

input_txt = "ASAP.txt"
output_pdf = "ASAP.pdf"

c = canvas.Canvas(output_pdf, pagesize=A4)
width, height = A4

y = height - 40

with open(input_txt) as f:
    for line in f:
        c.drawString(40, y, line.strip())
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

c.save()
print("PDF created:", output_pdf)