import PyPDF2 
import textract
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
'''
This file helps you classify documents.
For example you have a bunch of reasearch papers and wish to classify them.
Now use the power of machine learning to do your tedious work.
This program returns you a dictionary with filename as key and keywords as value
Now that your documents have been given keywords, go enjoy and dive in to your work.XD
'''

# Get all the PDF filenames in your working directory
PATH = os.path.abspath(os.path.dirname(__file__))
pdfFiles = []

for filename in os.listdir('.'):
   if filename.endswith('.pdf'):
     filepath=os.path.join(PATH, filename)
     pdfFiles.append(filepath)

textdict={}#initialize dictionary

for filename in pdfFiles:
    #filename = 'enter the name of the file here' 
    print('Analyzing file:',filename)
    #open allows you to read the file
    #pdfFileObj = open(filename,'rb')
    count = 0
    text = ""


    #we run the OCR library textract to #convert scanned/image based PDF files into text
    text = textract.process(filename, method='tesseract', language='eng')

    # Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.

    # Now, we will clean our text variable, and return it as a list of keywords.
    #The word_tokenize() function will break our text phrases into #individual words
    
    text=str(text, encoding='UTF-8')#convert byteoject to string
    tokens = word_tokenize(text)

    #we'll create a new list which contains punctuation we wish to clean
    punctuations = ['(',')',';',':','[',']',',']

    #We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords

    stop_words = stopwords.words('english')

    #We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.

    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    textdict[filename]+=[keywords]

print(textdict)

