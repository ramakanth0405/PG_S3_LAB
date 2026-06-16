from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep


titles = []
prices = []

page = 1
while page < 10:
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)
    if response.status_code == 404:
        break
    
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text[2:]
        titles.append(title)
        prices.append(price)

    page += 1
    sleep(1)

import pandas as pd
df = pd.DataFrame({'Title': titles, 'Price': prices})
print(df)