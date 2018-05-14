import PyPDF2

'''read back rb means'''
pdfFileObj = open('Pushplata.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()