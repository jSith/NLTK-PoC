# NLTK-PoC
A brief proof of concept of the NLTK package  
Overengineered so that readers can see some examples of objects, try blocks, and tests in Python

# Running This Code
1) Acquire the code from Git however you like (git clone, zip file, etc.)


2) The first time you run this, you'll want to uncomment the first two lines in sentiment_analysis.py.  
(comments in Python are done with a #)  
This will download the lexicon that the Vader package uses.  
After you've run it once with that, you can comment it back out again.  


3a) If you have an IDE like PyCharm, you can open test.py in PyCharm.  
Then click Run -> Run 'test'. Or you can click Run -> Run Unittests for Test.TestAnalysis. They do the same thing.  

3b) If you don't have an IDE set up, you can run it through the console as long as you have a Python interpreter.  
If you don't have Python, download it. https://www.python.org/downloads/  

If you're on Linux, you can just go to the console and enter python {path-to-this-project}/test.py  

If you're on Windows, find your Python installation. It should be called python.exe  
It normally goes into C:\Users\{username}\AppData\Local\Programs\Python.  
Then go to the command line and enter {path-to-Python-installation}\python.exe {path-to-this-project}\test.py  

4) Output  
You should see: "Ran 6 tests in {time}. OK"  
You can ignore the warning about the Twython library not being installed.  

5) Changing Stuff  
In test.py, you can change the values of the text strings in any of the tests or make a new test by copy-pasting.  
You can also change the threshold that the analyzer uses. Higher thresholds make neutral sentiments more likely.  
The threshold default is set to 0.3.  
You can change this by passing in an additional numerical parameter to analyze_sentiment.  
