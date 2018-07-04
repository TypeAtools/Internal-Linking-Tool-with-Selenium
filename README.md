<b>Internal Linking Tool for JS rendered pages</b>


InternalLinkingTooll_Selenium.py makes a Google site search for every keyword and determines if the URL we are analyzing is ranking for the selected keyword in Google (among the first 10 results for the ‘site:’ search). After that the code pulls in all the links from every Google result page and verifies if the URL we are analyzing is among them. If that is the case, that specific Google result page is internally linked to the URL we are analyzing, if it is not, then we should add a link. 

<b>Requirements</b>

For pages that are JavaScript rendered and the HTML is not fully accessible, we created a slightly different tool that uses Selenium for accessing the entire HTML of a webpage. The program works  a bit differently but in the end we get information about the internal linking of the page. The good news is this works not only for JS based websites but others as well. 

There are a few requirements for the code to work properly: 
- Python 3.6
- Chrome webdriver - you can download it here https://sites.google.com/a/chromium.org/chromedriver/downloads and place it in the folder where you keep your Python file. 
- Selenium ($pip install selenium)
- Google-api-python-client ($pip install google-api-python-client or if you have it installed already, just update it $pip install --upgrade google-api-python-client)
- Google api key and Google Search Engine ID number (https://support.google.com/customsearch/answer/2649143?hl=en) and Google Search Engine API key (https://developers.google.com/maps/documentation/javascript/get-api-key) 
- BeautifulSoup4 ($pip install bs4)
- Install requests ($pip install requests)
- Install lxml ($pip install lxml)
- Download sublime text https://www.sublimetext.com/3
- You have to have a .csv file with urls and keywords associated with it. The csv must have 3 columns, so one for the URL, the second for the keyword and a third one to be left empty. The data must be placed in the file starting with the second row. 


<b>How to use it?</b>

Inside the code, you will have to input a few things (see below):
- Chrome webdriver path on your computer
- Google Search Engine ID number (https://support.google.com/customsearch/answer/2649143?hl=en) and Google Search Engine API key (https://developers.google.com/maps/documentation/javascript/get-api-key) 
- The exact name of the CSV source file. In case you used the first part of the code the source file for this part of the analysis will be the destination file from PART I, otherwise the source file must be provided in .csv format, and must have 3 columns (url, keyword, and a third, empty column). 
- The name of the file must be written in the appropriate location inside the code - the place where the variable is defined - the name of the file should be put in parentheses, indicating the type of object (string) (source_csv = ‘destination.csv’). 
- The name of the destination CSV file.
- The names of the files must be written in the appropriate location inside the code - the place where the variable is defined - the name of the file should be put in parentheses, indicating the type of object (string) (detailed_report_destination=‘detailed_report.csv’). 
- The file can be named however you want, but it must differ from the source CSV file.
- The website address you are analysing. 


Once you’ve inserted all the data, run the code :) 


<b>The Detailed report will give you information about:</b>
- If the URL ranks for the given keyword in Google (PAGE RANKING IN GOOGLE FOR SELECTED KEYWORD?) and if the page needs to be optimized for selected keyword to start ranking in Google (NEED TO OPTIMIZE FOR SELECTED KEYWORD?)
- Gives you a list of Google Search Results for the site search for a selected keyword (GOOGLE SEARCH RESULTS)
- If Google result pages are internally linked to the URL (INTERNAL LINKING?)
- This report allows us to verify if the URL the keyword was associated with is ranking for the given keyword in Google. 
- If the URL is not among the results, then it should be optimized for the keyword it was associated with.
- The report also tells us if there is internal linking amongst the Google result pages and the URL we are analysing. If there is no internal linking, this should be amended, as google clearly thinks the pages should be connected - The pages ranking for identical keywords should be internally linked

<b>Possible problems/errors:</b>


- Exceptions:  The code should be ignoring most of the exceptions that could be thrown, but this means that in case of an exception the url that caused it will not be analyzed.
- Navigation links: 
This report includes ALL the links from the body of the HTML of a page, including the navigation etc. If you need to exclude the navigation some code must be added according  to what HTML tags are used in the website you want to analyse. 
Analysing a large number of URLs at once could cause Google to get suspicious and stop you from scraping google results until it verifies that you’re not a robot (which in this case you kind of are :) ). So try not to analyze more than 50 urls at once. 
- Other problems that we have not encountered  yet could pop up, if they do, leave a comment on GitHub and we will try to fix it. 
