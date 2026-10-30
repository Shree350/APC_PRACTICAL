from PyPDF2 import PdfMerger
pdf = PdfMerger()
pdf.append("260913_Analysis Dashboard.pdf")
pdf.append("260913_Case Studies.pdf")
pdf.write("file.pdf")
pdf.close()
print("PDFs merging was done successfully!")