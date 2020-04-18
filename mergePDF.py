import PyPDF2

pdfFiles = ["pdf1.pdf", "pdf2.pdf"]

#Iterate over pdf and open objects
pdfObjs = []
for pdfFile in pdfFiles:
    pdfFile = open(pdfFile, 'rb')
    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    pdfObjs.append([pdfFile, pdfRead])

#Create writer and add page from other docs
pdfWrite = PyPDF2.PdfFileWriter()
for pdfObj in pdfObjs:
    for pageNum in range(pdfObj[1].numPages):
        pageObj = pdfObj[1].getPage(pageNum)
        pdfWrite.addPage(pageObj)

#Write file out
pdfOut = open('final.pdf', 'wb')
pdfWrite.write(pdfOut)
pdfOut.close()

#Close initial files
for pdfObj in pdfObjs:
    for pageNum in range(pdfObj[1].numPages):
        pdfObj[0].close()