## installation
pip install gascoigne


# The Gascoigne package
a miscellaneous package of functions for python. Mostly dedicated to academic researchers.
For help and feedback please [open a github issue](https://github.com/gabrielepinto/gascoigne/issues).

So far we have: 
-coeffplot
-textdriller

## coeffplot
a python function to produce regression coefficient plot

for a list of examples  [see the notebook example here](https://github.com/gabrielepinto/gascoigne/blob/main/EXAMPLE_regplot.md)

from gascoigne import regplot
regplot.coeff_plot(a model or a list of model)

![png](output_25_0.png)



## textdriller
a python function to efficiently extract text from pdf and images.
It makes use of both ocr and canonical pdf text extractor. 
The main advantage of this function is that it can be used to extract text from a variety of sources (images, pdf, etc..) and uses the most appropriate and efficient tool depending on the type of source.
For example, if it is a scanned paper it will use ocr (quite slow), while if it is a machine-generated pdf it will use the canonical pdf text extractor.


![png](example_pdf_extractor.PNG)


for an example of its usage plese[ see here](https://github.com/gabrielepinto/gascoigne/blob/main/example_textdriller.md)



For help and feedback please [open a github issue](https://github.com/gabrielepinto/gascoigne/issues).