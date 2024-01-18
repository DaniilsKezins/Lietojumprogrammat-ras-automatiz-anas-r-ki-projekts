import PyPDF2
import fitz

pdf_file1=PyPDF2.PdfReader(open("parvaldnieks.pdf","rb"))
page1=pdf_file1.pages[0]
text1=page1.extract_text()

re1 = text1.find("Summa apmaksai:")
re2 = text1.find("EUR")
summa1=text1[re1+16:re2].rstrip()
summa1=summa1.replace(",", ".")
print("Summa par dzīvokli: "+summa1)

pdf_file2=PyPDF2.PdfReader(open("Rekins_Baltcom.pdf","rb"))
page2=pdf_file2.pages[0]
text2=page2.extract_text()

re3 = text2.find("Summa samaksai, EUR")
re4 = text2.find("Veicot apmaksu, lūgums norādīt pilnu rēķina numuru!")
summa2=text2[re3+20:re4].rstrip()
summa2=summa2.replace(",", ".")
print("Summa internetam: "+summa2)

with fitz.open("elektrum.pdf") as elektrum:
        page = elektrum[0]
        text3 = page.get_text()


re5 = text3.find("Rēķina summa ar PVN (EUR)")
re6 = text3.find("Rēķina Nr.")
summa3=text3[re5+26:re6].rstrip()
summa3=summa3.replace(",", ".")
print("Summa par elektrību: "+summa3)

summa4=float(summa1)+float(summa2)+float(summa3)
print("Kopējā summa: "+str(summa4))