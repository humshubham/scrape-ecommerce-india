# Scrape Indian e-commerce wesbistes

A library for scraping search results from popular shopping wesbites in India

## Requirements

Install python3 and run the following command in a terminal to install selectorlib and requests.

```python 
#for linux and macOs
pip3 install selectorlib
pip3 install requests

#for windows users
pip install pipenv
pip install requests
```

## Usage

1. Download and extract or git clone this repository

2. Cd into a website folder of your choice (e.g Amazon).

3. Visit the said website and copy a search url (or many) and place them in search_urls.txt.
e.g (Amazon)

```
https://www.amazon.in/s?k=sweatshirts&ref=nb_sb_noss
```

4. Open a terminal and run the search.py file.

```python
#for linux and macOs
python3 search.py

#for windows users
python search.py
```

5. The output will be stored in search_output.jsonl in json format.
```
//All search results will be in the following format
{"title": "Puma Men Sweatshirt", 
"url": "https://www.amazon.in/Puma-Mens-Sweatshirt-58397901_Medium-Heather/dp/B07YFDQ2ST/ref=sr_1_1?dchild=1&keywords=sweatshirts&qid=1615738164&sr=8-1", 
"rating": "4.7 out of 5 stars", 
"review_count": "4", 
"price": "594"}, 
```
5. In order to use the given source code for scraping other websites, edit selectorlib and place the respective css path of required element
```
//e.g : Amazon India
products:
    css: 'div[data-component-type="s-search-result"]'
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Text
        url:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Link
        rating:
            css: 'div.a-row.a-size-small span:nth-of-type(1)'
            xpath: null
            type: Attribute
            attribute: aria-label
        review_count:
            css: 'div.a-row.a-size-small span:nth-of-type(2)'
            xpath: null
            type: Attribute
            attribute: aria-label
        price:
            css: 'span.a-price:nth-of-type(1) span.a-offscreen'
            xpath: null
            type: Text
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Happy open sourcing.
