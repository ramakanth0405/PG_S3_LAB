from bs4 import BeautifulSoup
import requests

with open('PG_S3_IoT_0_sample_web.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    print(soup)