#Work with PDF file
# need to install PyPDF2 library on mac pip3 install PyPDF2

import PyPDF2 as pdf


def read_pdf(name):
    with open(name,'r+b') as f: 
        #create read object
        reader = pdf.PdfReader(f)
        print(f"File have {len(reader.pages)} pages")
        print(f"Autohor of file is {reader.metadata}")
        # Rread all content from document
        for page in range(0,len(reader.pages)):
            pageObj = reader.pages(page)
            print("\n" + pageObj.extractText())


read_pdf('recipe-book.pdf')


#ToDo to fix issue with pageObj = reader.pages(page)