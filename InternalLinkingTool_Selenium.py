# WHAT DOES THIS PROGRAM DO

# The prerequisite for running this code is having a csv with urls and Keywords to analyze ready in the form of a csv)
# With the ‘site: command search’ we search the website for each keyword and extract the first 10 results from google search.
# This step allows us to verify if the URL the keyword was associated with is among the results. It also tells us which pages are ranking for the given keyword in Google.
# If the URL is not among the results, then it should be optimized for the keyword it was associated with.
# In the next step we extract all the existing links from every google result page, so now we have an x number of URLs per google result URL.
# This step is important to get an insight of the internal linking structure of the page.
# We verify if the URL associated with the keyword is present in any of the links we pulled from the google result pages.
# The pages ranking for identical keywords should be internally linked
# Finally the pages from the google search results are sorted according to the presence of the main URL link on the page.
# The results are stored in a CSV.

# REQUIREMENTS
# PYTHON 3.6
# INSIDE TERMINAL THE FOLLOWING MODULES MUST BE INSTALLED (see the comments in 'importing all the necessary modules' below)

# IMPORTING ALL THE NECESSARY MODULES
# $pip3 install selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# $pip install bs4
from bs4 import BeautifulSoup
# $pip install lxml
import lxml
import unicodedata
import csv
#pip install requests
import requests
# pip install google-api-python-client
from googleapiclient.discovery import build


# DEFINING THE FUNCTIONS

# SPECIFY THE PATH TO CHROMEDRIVER ON YOUR COMPUTER! (if you don't know the path just drag the file from the Finder into Terminal and the path will pop up there) 
chrome_driver_path = '/Users/nina/Python/chromedriver'
# Define the function to get links
def get_links(url):
	browser = webdriver.Chrome(chrome_driver_path) 
	url = url
	browser.get(url)#navigate to the page
	innerHTML = browser.execute_script("return document.body.innerHTML")#returns the inner HTML as a string
	normal = unicodedata.normalize('NFKD', innerHTML).encode('ASCII', 'ignore')
	return normal


# Define the GoogleSearh function

def google_search(search_term):
	#specifying the location of the drivers for chrome
	browser = webdriver.Chrome(chrome_driver_path) 
	browser.get('http://www.google.com') # navigate to google
	search = browser.find_element_by_name('q')
	search.send_keys(search_term)
	search.send_keys(Keys.RETURN) # hit return after you enter search text
	innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
	normal = unicodedata.normalize('NFKD', innerHTML).encode('ASCII', 'ignore')
	return normal

# Define the function for the browser to close
def browser_quit():
	browser = webdriver.Chrome(chrome_driver_path) 
	browser.quit()



# DEFINIGN THE API SETTINGS


# Set up the Search Engine settings
search_engine_id = '010802131775339854406:vtjel4ckqew' #INSERT SEARCH ENGINE ID HERE
api_key = 'AIzaSyAFOs_d58cS_FE-Y678tyBwag3u7vqiRYM' #INSERT GOOGLE API KEY HERE

# DEFINING SOURCE AND DESTINATION CSVs

# define the source csv with URLs
source_csv = 'unilad_test.csv' # INSERT SOURCE CSV FILE HERE

csv_reader_file = open(source_csv, encoding='UTF-8')
csv_reader = csv.reader(csv_reader_file, delimiter=';')
# skip first line in the csv
next(csv_reader)

# Define the destination CSV for the detailed report
# INPUT DESTINATION CSV FILE FOR DETAILED REPORT HERE
detailed_report_destination = 'unilad_test_destination.csv' #INSERT DETAILED DESTINATION REPORT CSV FILE HERE

csv_writer_file = open(detailed_report_destination, 'w', newline='')
csv_writer = csv.writer(csv_writer_file, delimiter=';')
# write the column headers for the destination csv
csv_writer.writerow(['URL', 'PROG KEYWORD', 'USER KEYWORD', 'GOOGLE SEARCH RESULTS', 'PAGE RANKING IN GOOGLE FOR SELECTED KEYWORD?', 'NEED TO OPTIMIZE FOR SELECTED KEYWORD?', 'INTERNAL LINKING?', 'links all'])

# PREPARING OTHER SETTINGS

# define the URL of the website you want to search
site = 'https://www.unilad.co.uk' #INSERT SITE URL HERE - including http:// or https:// no trailing slash


# Prepare the list that will store all the links from the pagees of the Google Search results



# EXECUTING GOOGLE SITE SEARCH

# Go through all the URLs in the source CSV: - if the keyword was input manually, pick that, else, pick the programmaticaly defined keyword -
# call the Google Search function - create the URL by concatenating the site search, site and keyword and inputing the api key and search engine ID
# limiting the number of results to 10
 # Prepare a list for storing the results
# Go through all the results and choose which result from the google search to store, in this case we chose 'link' as we want to store the urls -
# store the results into the previously prepared list r1= [], so we can use it later

for item in csv_reader:
	r1 = []
	if item[2] == '':
        #results = google_search('site:' + site + ' ' + "'" + item[1] + "'", api_key, search_engine_id, cr='uk', start=1, num=10)
		results = google_search('site:' + site + ' ' + "'" + item[1] + "'")
	else:
        #results = google_search('site:' + site + ' ' + "'" + item[2] + "'", api_key, search_engine_id, cr= 'uk', start=1, num=10)
		results = google_search('site:' + site + ' ' + "'" + item[2])
	soup= BeautifulSoup(results, 'lxml')
	for a in soup.findAll('a',href=True):
		link = a['href']

		if link.startswith(site):
			if link.endswith('/'):
				link=link[:-1]
			r1.append(link)
		
				
	browser_quit()

	
    # Go through all the urls in the r1 list - make a dictionary to store all the items we will need later and give them appropriate names for the keys
	for google_res in r1:
		links_all = []
		r = {}
		r['url'] = item[0]
		r['prog_keyword'] = item[1]
		r['user_keyword'] = item[2]
		r['googles_results'] = google_res


# Verify if the original url is among the google search results - create 2 additionnal keys for the dictionary
# add values according to the presence of the URL in the google search results - if the URL is among the GSR the page is ranking in google for the given keyword
# and does not need optimizing, else it is not ranking and it does need optimizing

		if r['url'] in r1:
			r['ranking in google'] = 'page ranking for given keyword'
			r['need to optimize for selected keyword'] = 'no'
		else:
			r['ranking in google'] = 'page not ranking for given keyword'
			r['need to optimize for selected keyword'] = 'yes'


#EXTRACTING THE LINKS

#Now we want to get all the links for each page we got with the Google search function
#we call the get links function and go through every url we got from the google search
#We store the links into the previously prepared list so we can easily access them
#We veruify if the original url is among the extracted links: if it is, then the page is internaly linked, else is not and should be."""


		links = get_links(r['googles_results'])
		soup= BeautifulSoup(links, 'lxml')
		for a in soup.findAll('a', href=True):
			# extracting links from HTML tags using BS
			link = a['href']
			#print(link)
			if link.startswith(site):
				if link.endswith('/'):
					links_all.append(link[:-1]) 	
				else:
					links_all.append(link)	
			elif link.startswith('/'):
				if link.endswith('/'):
					links_all.append(site + link[:-1])	
				else:
					links_all.append(site+link)

			r['links_all'] = links_all
			
		matches=[]
		for links in links_all:
			#print (links)
			if links == r['url']:				
				matches.append(links)
		if len(matches)!= 0:
			print(matches)
			r['link present']='yes'
		else:
			r['link present'] = 'no'
				
		print(r['link present'])


# WRITING THE DATA TO CSVs

        # Finally we write all the data into a CSV named detailed report, which will have all the data we extracted
		try:
			csv_writer.writerow([r['url'], r['prog_keyword'], r['user_keyword'], r['googles_results'], r['ranking in google'], r['need to optimize for selected keyword'], r['link present'],r['links_all']])
		except Exception:
			csv_writer.writerow([r['url'], r['prog_keyword'], r['user_keyword'], r['googles_results'], r['ranking in google'], r['need to optimize for selected keyword'], 'error'])



csv_reader_file.close()
csv_writer_file.close()

