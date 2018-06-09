
from handleRequests import get_url
from bs4 import BeautifulSoup
import re 





# raw_html = handleRequests.get_url('https://bloomberg.com')
raw_html = get_url('https://bloomberg.com')
html = BeautifulSoup(raw_html, 'html.parser')


headers = html.find_all("a", class_='single-story-module__related-story-link')

headerArr = []; 


print('\n')


for j in headers:
	for z in j:
		headerArr.append(z)





for j in range(0, len(headerArr)):
	print(headerArr[j])



