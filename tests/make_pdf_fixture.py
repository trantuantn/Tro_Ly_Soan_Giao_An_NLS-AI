"""Create a self-authored test handout; not a textbook or official curriculum."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import sys

def make(path):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(path),pagesize=A4)
    c.setTitle('Synthetic handout - Comparing fractions')
    c.setAuthor('PRO 5.0 test fixture')
    y=790
    lines=[
        'SYNTHETIC TEST HANDOUT - NOT AN OFFICIAL TEXTBOOK',
        'Topic: Comparing fractions | Grade 6 | Page 1',
        'Planning duration: 45 minutes.',
        'Local lesson objective: compare two positive fractions using a common denominator.',
        'Example: 1/2 = 3/6; 2/3 = 4/6. Therefore 1/2 < 2/3.',
        'Practice: compare 3/4 and 5/8. Explain your method.',
        'Extension: find a fraction strictly between 1/2 and 2/3.',
        'Available resources: printed sheets; no Internet; no student devices.',
        'No official NLS codes or curriculum quotations are supplied.',
    ]
    for i,line in enumerate(lines):
        c.setFont('Helvetica-Bold' if i==0 else 'Helvetica',10)
        c.drawString(40,y,line);y-=34
    c.showPage();c.save()
if __name__=='__main__':make(sys.argv[1])
