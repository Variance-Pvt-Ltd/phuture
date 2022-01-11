
import urllib.request as urllib3
from bs4 import BeautifulSoup
URL = "https://www.nseindia.com/option-chain"
# r = requests.get(URL)
r = urllib3.urlopen(URL)
print(1)
soup = BeautifulSoup(r.content, 'html5lib')
print(2)

# print(soup.prettify())
ex=[]
list=soup.find('select', attrs= {'id':'expirySelect'})
for date in list.find_all('option'):
    ex.append(date)
print(ex)
# table = soup.find('div', attrs = {'id':'all_quotes'})
#
# for row in table.findAll('div',
#                          attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
#     quote = {}