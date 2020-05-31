from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pathlib import Path
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


# Read pdf
pdf_path=Path('/Users/mrajagopal/Documents/kubernetes-in-action.pdf')
pdf = PdfFileReader(str(pdf_path))
print(pdf.numPages)
print(pdf.documentInfo)
print(pdf.documentInfo.creator)
first_page = pdf.getPage(1)
#print(first_page.extractText())

# Extract pages from one pdf and write to another
pdf_path=Path('/Users/mrajagopal/Documents/Learning-Go-latest.pdf')
pdf = PdfFileReader(str(pdf_path))
with Path("/Users/mrajagopal/Documents/blank.pdf").open(mode="wb") as output_file:
    pdf_writer = PdfFileWriter()
    pdf_writer.addBlankPage(width=72, height=72)
    pdf_writer.addPage(pdf.getPage(1))
    pdf_writer.write(output_file)

# Extract multiple page and write
pdf_writer=PdfFileWriter()

for n in range(1,6):
    pdf_writer.addPage(pdf.getPage(n))
with Path("/Users/mrajagopal/Documents/blank2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# Extract multiple page and write
pdf_writer=PdfFileWriter()
for page in pdf.pages[1:4]:
    pdf_writer.addPage(page)

with Path("/Users/mrajagopal/Documents/blank3.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# merging pdf files
pdf_merge = PdfFileMerger()
pdf_path = Path("/Users/mrajagopal/Documents/pdfs")
files = list(pdf_path.glob("*.pdf"))
for file in files:
    pdf_merge.append    (str(file))

with Path("/Users/mrajagopal/Documents/pdfs/merge.pdf").open(mode='wb') as outputfile:
    pdf_merge.write(outputfile)

# Append pdf files
pdf_path=Path('/Users/mrajagopal/Documents/kubernetes-in-action.pdf')
pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
pdf_writer.addPage(pdf.getPage(1))
with Path("/Users/mrajagopal/Documents/pdfs/addpage.pdf").open(mode="wb") as outputfile:
    pdf_writer.write(outputfile)

merge_path = Path("/Users/mrajagopal/Documents/pdfs/merge.pdf")
page_path = Path("/Users/mrajagopal/Documents/pdfs/addpage.pdf")
pdf_merge = PdfFileMerger()
pdf_merge.append(str(merge_path))
pdf_merge.merge(1,str(page_path))

with Path("/Users/mrajagopal/Documents/pdfs/merge2.pdf").open(mode="wb") as outputfile:
    pdf_merge.write(outputfile)


# Rotate Pages
pdf_path=Path('/Users/mrajagopal/Documents/kubernetes-in-action.pdf')
pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
page1 = pdf.getPage(1)
page1.rotateClockwise(90)
pdf_writer.addPage(page1)
with Path("/Users/mrajagopal/Documents/pdfs/rotate.pdf").open(mode="wb") as outputfile:
    pdf_writer.write(outputfile)

#crop pages
pdf_path=Path('/Users/mrajagopal/Documents/kubernetes-in-action.pdf')
pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
page1 = pdf.getPage(1)
print(page1.mediaBox.upperLeft)
page1.mediaBox.upperLeft=(0,500)
pdf_writer.addPage(page1)
with Path("/Users/mrajagopal/Documents/pdfs/crop.pdf").open(mode="wb") as outputfile:
    pdf_writer.write(outputfile)

# Encrypting pdf
pdf_path=Path('/Users/mrajagopal/Documents/kubernetes-in-action.pdf')
pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
page1 = pdf.getPage(1)
pdf_writer.addPage(page1)
pdf_writer.encrypt(user_pwd="secret", owner_pwd='supersecret')
with Path("/Users/mrajagopal/Documents/pdfs/encrypt.pdf").open(mode="wb") as outputfile:
    pdf_writer.write(outputfile)


# Decrypting pdf
pdf_path=Path("/Users/mrajagopal/Documents/pdfs/encrypt.pdf")
pdf_writer = PdfFileWriter()
pdf = PdfFileReader(str(pdf_path))
pdf.decrypt(password="secret")
print("Test")
page1 = pdf.getPage(0)
print("Test2")
pdf_writer.addPage(page1)
with Path("/Users/mrajagopal/Documents/pdfs/decrypt.pdf").open(mode="wb") as outputfile:
    pdf_writer.write(outputfile)


canvas = Canvas("/Users/mrajagopal/Documents/pdfs/font-colors.pdf", pagesize=LETTER)

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "Blue text")

# Save the PDF file
canvas.save()







