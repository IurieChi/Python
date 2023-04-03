#Work with PDF file
# need to install PyPDF2 library on mac pip3 install PyPDF2

import PyPDF2 as pdf
from PIL import Image
import os, fitz, pdfplumber



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
        reader = pdf.PdfReader(f)
        for i in range(0,len(reader.pages)):
            page = reader.pages[i]
            for img in page.images:
                # imagename = os.path.splitext(files/images)
                # imagename = f'image_{str(img)}.png'
                with open(os.path.join('files/images/',img.name),'wb')as out: 
                    out.write(img.data)    
          
    
    # #extract image from  file using fitz module
def extract_image_fitz(file):
    pdf_file = fitz.open(file) #create objet 
    images_list =[] # create list to store image info
    for page in range(0, len(pdf_file)):
        page_content = pdf_file[page]
        images_list.extend(page_content.get_images())
    if len(images_list)==0: 
        raise ValueError (f'PDF file {file} dont contain Images')
    # Extract and save images
    for i, image in enumerate(images_list, start=1):
        xref= image[0]# extract image object number 
        image = pdf_file.extract_image(xref) #extract image
        image_bytes= image['image']
        image_ext = image['ext'] #store image extension 
        image_name = str(i)+'.'+ image_ext #generate image name 
        with open(os.path.join('files/images/',image_name),'wb')as ext_file:
            ext_file.write(image_bytes)
            ext_file.close()

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

def extract_tabel(file): # need to install pdfplumber and import it 
    with pdfplumber.open(file) as f:
        for page in f.pages:
            print(page.extract_tables())

def save_PDF_toImage(file, page:int):#you need to install the PyMuPdf  pip install --upgrade pymupdf then import fitz
    doc = fitz.open(file)
    page = doc.load_page(page)
    # for i in range(0,len(page)):
    pix = page.get_pixmap()
    pix.save (f'page_{page.number}.png')

    # #save all the pages as images
    # for i in range(doc.page_count):
    #     page = doc.load_page(i)
    #     pix = page.get_pixmap()
    #     pix.save("page-%i.png" % page.number)
    
def extract_links(file): #you need to install the PyMuPdf  pip install --upgrade pymupdf then import fitz
    doc = fitz.open(file)
    for i in range(doc.page_count):
        page = doc.load_page(i)
        link = page.get_links()
        print(link)
    


# get_metadata_pdf('files/recipe-book.pdf')
# read_pdf('files/pdf/recipe-book.pdf')
# split_pdfs('files/pdf/recipe-book.pdf')
# get_up_to_page('files/pdf/recipe-book.pdf',0,3)
# get_lat_page('files/pdf/recipe-book.pdf')
# list = get_list_of_files("files/pdf")
rotate_page('files/pdf/recipe-book_from_0_to_3.pdf',2)
# extract_tabel('files/pdf/recipe-book.pdf')
# extract_images('files/pdf/recipe-book.pdf')
# save_PDF_toImage('files/pdf/recipe-book.pdf',4)
# extract_links('files/pdf/recipe-book.pdf')
