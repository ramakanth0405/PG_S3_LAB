from bs4 import BeautifulSoup
import requests

with open('PG_S3_IoT_0_sample_web.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

    # To print full structure
    print(soup) 

    # Prints with structure
    print(soup.prettify()) 

    # To print div
    match = soup.div 
    print(match)

    # To print title
    print(soup.title)

    # To print footer div
    match_2 = soup.find('div', class_='footer') 
    print(match_2)

    # Extracting Articles
    article = soup.find('div', class_='article')
    print(article.h2.a.text) # To print article title
    print(article.p.text) # To print article description

    # Using a loop to print the articles
    for article in soup.find_all('div', class_='article'):
        headline=article.h2.a.text
        print(headline)
        summary=article.p.text
        print(summary)
    
    # To print the first anchor tag
    anchor_tag = soup.a
    print(anchor_tag) 

