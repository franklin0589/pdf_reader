# importing required modules
import PyPDF2

def request_input():
    input_file = input("Whats the input file name?\t")
    firstpage = int(input("What is the starting page in the range?\t"))
    endpage = int(input("What is the last page in the range?\t"))
    return (input_file, firstpage, endpage)

def parse_pdf(inputs):
    # creating a pdf file object
    pdfFileObj = open(inputs[0], 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    num_of_pages = pdfReader.numPages
    mytext = ""
    # creating a page object
    for x in range(inputs[1], inputs[2]):
        pageObj = pdfReader.getPage(x)
        # extracting text from page
        mytext += pageObj.extractText()

    # closing the pdf file object
    pdfFileObj.close()
    return mytext

def split_text(text):
    clustered = text.split('\n')
    return [x for x in clustered if x.strip()]
