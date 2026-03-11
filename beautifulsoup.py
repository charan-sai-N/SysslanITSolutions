'''BeautifulSoup is a Python library used for parsing HTML and XML documents.
 It helps developers extract data from web pages easily, which is a common task in web scraping and data collection projects.
 BeautifulSoup is mainly used to:

Extract data from websites

Parse HTML and XML documents

Navigate webpage structure (tags, attributes, text)

Clean and organize scraped data'''



import requests
from bs4 import BeautifulSoup

url = "https://resumeworded.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h3") ## finds this in website
print(title.text)