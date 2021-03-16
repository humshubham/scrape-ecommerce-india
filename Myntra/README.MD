# Scrape Myntra

A library for scraping search results from Myntra.com

## Requirements

Install python3 and run the following command in a terminal to install selectorlib and requests.

```python 
#for linux and macOs
pip3 install requests

#for windows users
pip install requests
```

## Usage

1. Download and extract or git clone this repository

2. Cd into a website folder of your choice (e.g Amazon).

3. Visit the said website and copy a search url (or many) and place the variable url.
e.g 

```
url = 'https://www.myntra.com/sweatshirts&plaEnabled=false'
```

4. Open a terminal and run the myntra.py file.

```python
#for linux and macOs
python3 myntra.py

#for windows users
python myntra.py
```

5. The output will be stored in search_output.jsonl in json format.
```
//All search results will be in the following format
{
    "url":"https://www.myntra.com/Sweatshirts/HRX-by-Hrithik-Roshan/HRX-by-Hrithik-Roshan-Men-Green-Solid-Rapid-Dry-Antimicrobial-Training-Sweatshirt/12527376/buy",
    "title":"HRX by Hrithik Roshan Men Green Solid Rapid-Dry Antimicrobial Training Sweatshirt",
    price":764,
    "image":"http://assets.myntassets.com/assets/images/12527376/2021/3/5/16b13c67-c4fd-4ccf-9921-44ff526166551614948712797-HRX-by-Hrithik-Roshan-Men-Green-Solid-Rapid-Dry-Antimicrobia-1.jpg",
    "ratings":5
}, 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Happy open sourcing.
