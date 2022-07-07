import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


r = requests.get(url)
htmlContent = r.content


soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title


paras = soup.find_all('p')

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        # print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

elem = soup.select('#loginModal')
print(elem)
