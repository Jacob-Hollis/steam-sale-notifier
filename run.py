import bs4 as bs
import urllib.request
import xml
import ssl

url_string = 'https://gg.deals/game/sea-of-thieves/'

#creating the connection and context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#opening the connection
my_url = urllib.request.urlopen(url_string, context=ctx).read()

#turning the html into a beautifulsoup object
soup = bs.BeautifulSoup(my_url, 'lxml')
def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

data_discounts = (soup.find_all('alt', {'Steam'}))
data_body = (soup.find_all('span', {'class':'title'}))
print (data_discounts)