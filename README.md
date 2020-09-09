# Predict-It-betting-site-scrape
This takes different markets from the predicit-it website, and gives you an overview of which markets are not balanced

How to:
Go to https://www.predictit.org/markets scroll to the bottom of the page to show all the markets, and with inspect element on chrome, right click where it says 
"html" should be right at the top, then copy->copy element. Create a new file in any text editor and call it "%mm-%dd-%yyyy.html" using your current date, paste the 
copied html code into "%mm-%dd-%yyyy.html". Save "%mm-%dd-%yyyy.html" in the same folder as the python file you download, "PredictItScraper.py". Now just run 
"PredictItScraper.py", the resulting txt file will be in the same folder as mentioned before.

From running the program over multiple weeks, it is best to find values around -10 to -2, these are markets where there are two options to bet on and if they do not 
up too 100 then you can buy both yes, or both no, and this will lead to small profits. 
