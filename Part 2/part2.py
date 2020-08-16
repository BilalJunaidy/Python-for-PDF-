##PART 2 - PYTHON FOR PDF TUTORIAL SERIES:

##Code Explainer:
##In the following line of code we are importing the PyPDF2 library (the one which we had
##downloaded in the part 1 of this Tutorial. From this library we are specifically importing
##the PdfFileReader Class which allows us to read pdf documents.

from PyPDF2 import PdfFileReader as pdfreader

##Code Explainer:
##In the following line of codes, we are opening the "meetingminutes.pdf" pdf file and
##referring to the file as "myfile", and this file is being opened using read binary method
##because a pdf document has a binary format. 
##"myfile" specifically, represents the bytes of information included in the
##"meetingminutes.pdf" pdf document.

with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\meetingminutes.pdf','rb') as myfile:

##Code Explainer:
##In the following line of code, we are passing the information stored into the "myfile" variable into
##the pdfreader class. This pdfreader class will then return a pdfreaderobject, upon which we will be
##able to perform various functions.
##In simple words, this pdfreaderobject represents this "meetingminutes.pdf"

    pdfreaderobject = pdfreader(myfile)
##
    Number_of_pages = pdfreaderobject.getNumPages()
    print(f'The number of pages are\n: \n{Number_of_pages}')

    global_information = pdfreaderobject.getDocumentInfo()

    print(f"""
          The author of this pdf is: {global_information.author}
          The creator of this pdf is: {global_information.creator}
          The producer of this pdf is: {global_information.producer}
          The subject of this pdf is: {global_information.subject}
          The title of this pdf is: {global_information.title}
          """)

    print(f"This pdf is encrypted: {pdfreaderobject.isEncrypted}")
    
##Code Explainer:
##Applying the getPage(i) where i represents the index of the page number you would like to get, returns
##a pdfpageobject.
##In simple words, a pdfpageobject can be thought of as representing a specific page in our
##"meetingminutes.pdf" pdf document.

    seventh_page = pdfreaderobject.getPage(6)
    seventh_page_text = seventh_page.extractText()
    print(f"The following is the text on the seveth page : \n{seventh_page_text}")

    for i in range(Number_of_pages):
        pageobject = pdfreaderobject.getPage(i)
        print(pageobject.extractText())

