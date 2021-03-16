
import requests
import json
import math

s = requests.Session()

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
url = 'https://www.myntra.com/sweatshirts&plaEnabled=false'
response = s.get(url, headers = headers, timeout = 10)


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
url = 'https://www.myntra.com/gateway/v2/search/sweatshirts?plaEnabled=false&rows=100&o=0'
response = s.get(url, headers = headers, timeout = 10)


data = json.loads(response.text)
data_products = data['products']
final_products = []
products={}
for product in data_products:
    products['url'] = "https://www.myntra.com/" + product["landingPageUrl"]
    products['title'] = product["productName"]
    products['price'] = product["price"]
    products['image'] = product['searchImage']
    products['ratings'] = math.ceil(product['rating'])
    final_products.append(products)




with open("search_output.jsonl", "w") as outfile:
    json.dump(final_products, outfile)
