import requests
from bs4 import BeautifulSoup

url = "https://resumeworded.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h")
print(title.text)