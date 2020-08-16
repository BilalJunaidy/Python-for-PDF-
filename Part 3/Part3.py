####THE FOLLOWING ARE EXAMPLES OF WRITING TO PDF FILES, OR RATHER COPYING FROM ONE PDF TO ANOTHER.
##
####Code Explainer:
####Importing the PdfFileReader and the PdfFileWriter class from the PyPDF2 library.
####The PdfFileWriter class is going to be used in writing to pdf files.
##
from PyPDF2 import PdfFileReader as pdfreader
from PyPDF2 import PdfFileWriter as pdfwriter
####
####Code Explainer:
####This is creating a pdfwriter object which is going to represent the new pdf document which we are
####trying to create. We are calling this pdfwriter object as pdfWriter in our code below.
##
pdfwriterobject = pdfwriter()
####
####Code Explainer:
####Opening up the file pdf document in read binary mode and then passing the read_1 stream into the
####pdfreader reader class to return the pdf.
##
with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\meetingminutes.pdf', 'rb') as read_1:
    pdfreaderobject = pdfreader(read_1)
    Number_of_pages = pdfreaderobject.getNumPages()
    for i in range(Number_of_pages):
        page = pdfreaderobject.getPage(i)
##
####Code Explainer:
####In this line of code, we are essentially (for each iteration) adding the page object that we have
####created in the line above and using the addPage method to add that page into our pdfwriterobject.
####Since we are iterating through each page in our initial pdf document, we are basically adding
####each page in that document into this pdfwriterobject. 
####
        pdfwriterobject.addPage(page)
##
####Code Explainer:
####In these lines of code, we are creating a new pdf document called "part3.pdf" and opening it up in
####the "wb" mode(or in the other words, write binary mode.)
####As discussed previously, the reason for doing this is because the pdf document has a binary format
####and hence requires us to write it in a binary mode.

        with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\Part 3\part3.pdf', 'wb') as outputfile:
          pdfwriterobject.write(outputfile)
##

##THE FOLLOWING IS AN EXAMPLE OF ROTATING PAGES

from PyPDF2 import PdfFileReader as pdfreader
from PyPDF2 import PdfFileWriter as pdfwriter

pdfwriterobject = pdfwriter()

with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\IAMGOLDFS.pdf', 'rb') as file:
    pdfreaderobject = pdfreader(file)
    Number_of_pages = pdfreaderobject.getNumPages()
    for i in range(Number_of_pages):
      pdfpageobj = pdfreaderobject.getPage(i)
##
####Code Explainer:
####After getting the ith page object, we are applying a rotateclockwise() method and passing into it
####the degree of rotation as an argument (which is 180 in this example).
      pdfpageobj.rotateClockwise(180) 
      pdfwriterobject.addPage(pdfpageobj)

    with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\Part 3\IAMGOLDFS_rotated.pdf', 'wb') as writefile:
        pdfwriterobject.write(writefile)



##THE FOLLOWING IS AN EXAMPLE OF ADDING CUSTOM WATERMARKS IN A PDF DOCUMENT

from PyPDF2 import PdfFileReader as pdfreader
from PyPDF2 import PdfFileWriter as pdfwriter
import os
##
file_dir = r'C:\Users\bilal\Desktop\Python PDF Tutorial'
main_file_name = "meetingminutes.pdf"
main_file_path = os.path.join(file_dir, main_file_name)


secondary_file_name = "watermark.pdf"
secondary_file_path = os.path.join(file_dir, secondary_file_name)

pdfwriterobject = pdfwriter()
##
##Code Explainer:
##Instead of having to open two files in two different lines of code, we have simply combined the
##operation of opening both of the files up in one line of code below.
with open(main_file_path, 'rb') as read_file_1, open(secondary_file_path, 'rb') as read_file_2:
    pdfreaderobject_1 = pdfreader(read_file_1)
    page_1 = pdfreaderobject_1.getPage(0)

    pdfreaderobject_2 = pdfreader(read_file_2)

    page_1.mergePage(pdfreaderobject_2.getPage(0))

    pdfwriterobject.addPage(page_1)

    with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\Part 3\watermarkedpage.pdf', 'wb') as write_file:
        pdfwriterobject.write(write_file)


