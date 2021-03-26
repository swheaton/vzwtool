#from PyPDF2 import PdfFileReader
import pdfminer.high_level

print(extract_text("bill.pdf"))
#reader = PdfFileReader("bill.pdf")

#print(str(reader.getPage(0).extractText()))
