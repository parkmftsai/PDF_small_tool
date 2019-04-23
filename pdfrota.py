import PyPDF2
minutesFile = open('1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
                           
pdfWriter = PyPDF2.PdfFileWriter()

page = pdfReader.getPage(0)
#page.rotateClockwise(-90)
pdfWriter.addPage(page)
page = pdfReader.getPage(1)
page.rotateClockwise(-90)
pdfWriter.addPage(page)

resultPdfFile = open('rotatedpage.pdf','wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()


