#Work with PDF file
# need to install PyPDF2 library on mac pip3 install PyPDF2

import PyPDF2 as pdf
import os, fitz



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
 #extract image from file        
def extract_images(file):
    with open(file,'rb') as f:
        reader = pdf.PdfMerger(f)
        for i in range(0,len(reader.pages)):
            page = reader.pages[i]
            count = 1
            for img in page.images:
                filename = os.path.splitext(file)
                imagename = f'{filename} image_{str(count)}.png'
                with open(imagename, "wb") as fp:
                    fp.write(img.data)   
                    count+=1    


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
            newfilename = f'{filename} page_{page+1}.pdf'
            #save vile in PDF
            with open (newfilename, 'wb') as out:
                writer.write(out)
        print(f"Created a pdf {newfilename}")

 # get pdf up to particulary page 
def get_up_to_page(file, start_page:int=0,stop_page:int= 0):
    with open(file, 'rb')as f:
        reader = pdf.PdfReader(f)
        writer = pdf.PdfWriter()
        for page in range(start_page,stop_page):
            selected_page = reader.pages[page]
            writer.add_page(selected_page)# add page to writer 
            filename = os.path.splitext(file)[0]
            newFillname = f'{filename}_from_{start_page}_to_{stop_page}.pdf'
        # Create new file and write on 
        with open (newFillname, 'wb') as output:
            writer.write(output)
        print(f'New file {newFillname} has been created, from {file} from page {start_page} to {stop_page}')

# split off last page from PDF
def get_lat_page(file):
    with open(file, 'rb')as f:
        reader = pdf.PdfReader(f)
        writer = pdf.PdfWriter()
        last_page = reader.pages[len(reader.pages)-1] #find last page 
        writer.add_page(last_page)
        filename = os.path.splitext(file)[0]
        newFillname = f'{filename}_lastPage.pdf'
    with open(newFillname, 'wb') as out:
        writer.write(out)
    print(f'New file with last page from {file} has been created')

#get a list of pdf liles from directory.
def get_list_of_files(folder: str):
    pdf_list =[]
    for path, subdirs,files in os.walk(folder):
        for name in files:
            if name.endswith('.pdf'):
                pdf_list.append(os.path.join(path,name))
    # print(pdf_list)
    return pdf_list

#Merging PDFS
def pdf_merge(list_of_pdf, output_filename='Merege_pdfs.pdf'):
    merger =pdf.PdfMerger()
    with open(output_filename, 'wb')as out:
        for file in list_of_pdf:
            merger.append(file)
        merger.write(out)


#to fix issue with index errror 
#rotate page to 90 or 180 degree
def rotate_page(file, page: int, rotation:int = 90):
    with open(file,'rb')as f:
        reader = pdf.PdfReader(f)
        writer = pdf.PdfWriter()
        writer.add_page(reader.pages[page])
        #rotate
        writer.pages[page].rotate(rotation) 
        filename = os.path.splitext(file)[0]
        newFilename = f'{filename}_rotated_page_{page}_to_{rotation}_degree.pdf'
        with open(newFilename,'wb')as out:
            writer.write(out)
    print("document created ")

# def extract_links(file): #you need to install the PyMuPdf  pip install --upgrade pymupdf then import fitz


# get_metadata_pdf('files/recipe-book.pdf')
# read_pdf('files/pdf/recipe-book.pdf')
# split_pdfs('files/pdf/recipe-book.pdf')
# get_up_to_page('files/pdf/recipe-book.pdf',0,3)
# get_lat_page('files/pdf/recipe-book.pdf')
# list = get_list_of_files("files/pdf")
# rotate_page('files/pdf/recipe-book_from_0_to_3.pdf',2)
extract_images('files/pdf/recipe-book.pdf')
