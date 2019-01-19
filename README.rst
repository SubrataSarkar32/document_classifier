==============
document_classifier
==============
document classification using machine learning and OCR.Prints the keywords of document

License
=======

Copyright [2019] [Subrata Sarkar]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Usage
=====
for now,
paste the PDF files inside of document_classifier folder
run `readpdf2.py`
A dictionary is printed

OR

use this script in your pdf folder:
.. code-block:: python
::

    import os    
    import document_classifier    
    PATH = os.path.abspath(os.path.dirname(__file__))    
    files = []    
    for filename in os.listdir('.'):    
        if filename.endswith('.pdf'):        
            filepath=os.path.join(PATH, filename)            
            files.append(filepath)            
    dict1=document_classifier.analyze(pdfFiles=files)    
    print(dict1)

Installation
=====
This library works on Windows(Python3).You need to install Tesseract-OCR and nltk packages.
Link to Tesseract(https://github.com/UB-Mannheim/tesseract/wiki)<version 4 preferrably>
For nltk:
    go to python IDLE:
::

    >>>import nltk
    
    >>>nltk.download()
    
This will open a new window.
Download the packages you need.If you are not sure just click on all packages and install


Install via pip:
    `pip install git+ssh://git@github.com/SubrataSarkar32/document_classifier.git@master`
OR
    1.Dowload zip
    
    2.open cmd in document_classifier directory
    
    3.type : `python setup.py install` 

Contribute
=====
    
1.Fork the repo
    
2.Make changes
    
3.Make a pull request
