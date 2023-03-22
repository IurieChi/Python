#Work with PDF file
# need to install PyPDF2 library on mac pip3 install PyPDF2

import PyPDF2 as pdf
import os 



def get_metadata_pdf(name):
    with open(name,'rb') as f: 
        #create read object
        reader = pdf.PdfReader(f)
        info = reader.metadata
        print(f"Title '{info.title}' ")
        print(f"File have {len(reader.pages)} pages")
        print(f"Autohor of file is {info.author}")
        print(f"Create date is {info.creation_date}")

def read_pdf(name):
    with open(name,'rb') as f: 
        #create reader object
        reader = pdf.PdfReader(f)
        result =[]
        # Rread all content from document
        for i in range(0,len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            result.append(text)
        print(' '.join(result))# convert list to a sting 

#Split PDFs 
# split pdf into multiple pdfs save 1 page per file
def split_pdfs(file):
    with open(file, 'rb') as f:
        reader = pdf.PdfReader(f)
        for page in range(0,len(reader.pages)):
            selecteg_page = reader.pages[page]
            #create new file and write 
            writer = pdf.PdfWriter()
            writer.add_page(selecteg_page) #create conection on reader and writer 
            filename = os.path.splitext(file)[0]
            newfilename = f'{filename}{page+1}.pdf'
            #save vile in PDF
            with open (newfilename, 'wb') as out:
                writer.write(out)
        print(f"Created a pdf {newfilename}")
        



# split off last page for signature 
# get pdf up to particulary page 




# get_metadata_pdf('files/recipe-book.pdf')
# read_pdf('files/pdf/recipe-book.pdf')
# split_pdfs('files/pdf/recipe-book.pdf')

