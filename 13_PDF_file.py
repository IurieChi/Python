#Work with PDF file
# need to install PyPDF2 library on mac pip3 install PyPDF2

import PyPDF2


def read_pdf(name):
    with open(name,'r+b') as f:
        #create read object
        reader = PyPDF2.PdfFileReader(f)
        print(f"File have {reader.numPages} pages")
        print(f"Autohor of file is {reader.getDocumentInfo()}")
        # Rread all content from document
        for page in range(0,reader.numPage):
            pageObj = reader.getPage(page)
            print("\n" + pageObj.extractText())


read_pdf('recipe-book.pdf')
