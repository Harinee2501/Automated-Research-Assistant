import requests
from bs4 import BeautifulSoup

def fetch_webpage_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    paragraphs=soup.find_all('p')
    content='\n'.join([para.get_text() for para in paragraphs])
    return content