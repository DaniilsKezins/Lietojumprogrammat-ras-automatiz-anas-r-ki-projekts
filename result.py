import PyPDF2
import pathlib

pdf_file=PyPDF2.PdfReader(open("elektrum.pdf","rb"))
number_of_pages=len(pdf_file.pages)
page1=pdf_file.pages[0]
page2=pdf_file.pages[1]
text1=page1.extract_text()
text2=page2.extract_text()

print(text1)
