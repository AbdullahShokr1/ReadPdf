# importing the required modules
import PyPDF2

def PDFrotate(filepath, newFileName):

	# creating a pdf File object of original pdf
        pdfFileObj = open(filepath, 'rb')

	# creating a pdf Reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        pdfWriter = PyPDF2.PdfFileWriter()
        #nuber of pages
        pagenum = []
        for x in range(pdfReader.numPages):
                a = pagenum.append(x+1)
	#Take the number of page from User
        numberOfPage = input('From which page do you want to extract the data?'+"("+str(pagenum)+"or, all): ")
        try:
            val = int(numberOfPage)
            if int(numberOfPage) <= (x+1):
                pageObj = pdfReader.getPage(int(numberOfPage)-1)
                pagecontent = pageObj.extractText('waiting')
                pdfWriter.addPage(pagecontent)
            else:
               for page in range(pdfReader.numPages):
                     # creating rotated page object
                     pageObj = pdfReader.getPage(page)
                     # adding rotated page object to pdf writer
                     pdfWriter.addPage(pageObj)
        except ValueError:
            for page in range(pdfReader.numPages):
                     # creating rotated page object
                     pageObj = pdfReader.getPage(page)
                     # adding rotated page object to pdf writer
                     pdfWriter.addPage(pageObj)  
	# new pdf file object
        newFile = open(newFileName, 'wb')

	# writing rotated pages to new file
        pdfWriter.write(newFile)

	# closing the original pdf file object
        pdfFileObj.close()

	# closing the new pdf file object
        newFile.close()


def main():
        print(" <============= created by Abdullah Shokr =============>   ")
        print("            <============Hello============>                ")
        #The file Path
        filepath = input('Enter File Path end by .pdf :')
 
        # new pdf file name
        newFileName = 'rotated_example1.pdf'
     
        # calling the PDFrotate function
        PDFrotate(filepath, newFileName)
if __name__ == "__main__":
    # calling the main function
    main()
