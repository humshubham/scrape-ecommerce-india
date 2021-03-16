import selectorlib
from selectorlib import Extractor
import requests
import json
from time import sleep
from fake_useragent import UserAgent


# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('search.yml')


def scrape(url):
    ua = UserAgent()

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.bewakoof.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s" % url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Flipkart data please contact" in r.text:
            print(
                "Page %s was blocked by Flipkart. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (
                url, r.status_code))
        return None
    # Pass the HTML of the page and create
    #with open("output.html", "w") as outfile:
    #    outfile.write(r.text)
    return e.extract(r.text)

#scrape('https://www.bewakoof.com/search/sweatshirts?ga_q=sweatshirts')



# product_data = []
with open("search_urls.txt", 'r') as urllist, open('search_output.jsonl', 'w') as outfile:
    for url in urllist.read().splitlines():
        data = scrape(url)

        if data:
            print(data['products'])
'''            for product in data['products']:
                
                product['url'] = 'https://www.bewakoof.com' + product['url']
                    
                json.dump(product, outfile)
                outfile.write(", \n")
'''                # sleep(5)
