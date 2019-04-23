import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time


def getFileName(filedir):
    """
    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    
    """
    file_list=["1.pdf","2.pdf","3.pdf","4.pdf","5.pdf"]
    return file_list if file_list else []

def MergePDF(filepath, outfile):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    if pdf_fileName:
        for pdf_file in pdf_fileName:
            print("PATH:%s"%pdf_file)

            
            input = PdfFileReader(open(pdf_file, "rb"))

            
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("Page:%d"%pageCount)

           
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))

        print("all page:%d."%outputPages)
     
        outputStream = open(os.path.join(filepath, outfile), "wb")
        output.write(outputStream)
        outputStream.close()
        print("PDF combine is done")

    else:
        print("error")


def main():
    time1 = time.time()
    file_dir = r'./' 
    outfile = "Cheat_Sheets.pdf" 
    MergePDF(file_dir, outfile)
    time2 = time.time()
    print('cost time:%s s.' %(time2 - time1))

main()
