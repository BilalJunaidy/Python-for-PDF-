##OPENING AND READING PDF DOCUMENTS - INTRODUCTION TO THE FOLLOWING CONCEPTS:
## 1. THE USE OF THE FILE CONTEXT MANAGER
## 2. STREAM
## 3. THE REASON FOR ADDING 'r' BEFORE ADDING THE FILE PATH
## 4. VARIOUS METHODS OF WORKING WITH MULTI-LINE STRINGS IN PYTHON 
## 5. OPENING THE FILE IN READ BINARY FORMAT AND NOT JUST READ
## 6. UNDERSTANDING THE PDF READER OBJECT AND ITS MOST COMMON METHODS 
## 7. UNDERSTANDING THE PDF PAGE OBJECT AND ITS MOST COMMON METHODS
## 8. THE CHALLENGES OF EXTRACTING TEXT WITH PYPDF2 AND ALTERNATIVES


from PyPDF2 import PdfFileReader as pdfreader



with open(r'C:\Users\bilal\Desktop\Python PDF Tutorial\meetingminutes.pdf', 'rb') as file:
    pdfreaderobject = pdfreader(file)

    Number_of_pages = pdfreaderobject.getNumPages()
    print(f'The number of pages are: {Number_of_pages}')

    global_information = pdfreaderobject.getDocumentInfo()

    print(f"""
          The author of this pdf is: {global_information.author}
          The creator of this pdf is: {global_information.creator}
          The producer of this pdf is: {global_information.producer}
          The subject of this pdf is: {global_information.subject}
          The title of this pdf is: {global_information.title}
          """)

    print(f"This pdf is encrypted: {pdfreaderobject.isEncrypted}")
    
    
    first_page = pdfreaderobject.getPage(6)
    first_page_text = first_page.extractText()
    print(f"The following is the text on the first page : \n{first_page_text}")

    for i in range(Number_of_pages):
        pageobject = pdfreaderobject.getPage(i)
        print(pageobject.extractText())
