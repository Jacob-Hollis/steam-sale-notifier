import bs4 as bs
import urllib.request
import xml
import ssl

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

#lets find all the price divs
for div in soup.find_all('div', 'similar-deals-container items-with-top-border-desktop'):
    #in those divs, lets find the images (the only source of the store names)
    #search for the store name which is in the alt tags
    img = div.find('img', alt=True)
    #if we find the name of our store in the img string, continue with the search
    if ("steam" in str(img).lower()):
        #find the div wrapping the image
        wrapping_div = img.find_previous('div', 'relative hoverable-box d-flex flex-wrap flex-align-center game-item cta-full item game-deals-item game-list-item keep-unmarked-container')
        #find the div that wraps the price
        inner_div = wrapping_div.find('div', 'game-info-wrapper relative')
        #find the price div
        price_div = inner_div.find('div', 'price-wrapper')
        #find the span with the price
        price_span = price_div.find('span', 'price-inner game-price-current')
        #convert the price to decimal and remove dollar sign
        price_decimal = float(price_span.text[1:])
        #check whether it is on sale
        on_sale = price_decimal < normal_price

        print ('Price: $' + str(price_decimal))
        print ('On Sale: ' + str(on_sale))
