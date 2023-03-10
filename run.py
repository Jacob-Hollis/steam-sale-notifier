import bs4 as bs
import urllib.request
import xml
import ssl
from decimal import Decimal

url_string = 'https://gg.deals/game/sea-of-thieves/'
normal_price = 39.99

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

for div in soup.find_all('div', 'similar-deals-container items-with-top-border-desktop'):
    img = div.find('img', alt=True)
    if ("steam" in str(img).lower()):
        wrapping_div = img.find_previous('div', 'relative hoverable-box d-flex flex-wrap flex-align-center game-item cta-full item game-deals-item game-list-item keep-unmarked-container')
        inner_div = wrapping_div.find('div', 'game-info-wrapper relative')
        price_div = inner_div.find('div', 'price-wrapper')
        price_span = price_div.find('span', 'price-inner game-price-current')
        price_decimal = float(price_span.text[1:])
        on_sale = price_decimal < normal_price
        print ('Price: $' + str(price_decimal))
        print ('On Sale: ' + str(on_sale))
