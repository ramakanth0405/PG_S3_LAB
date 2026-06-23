from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import random

def scrape_pages(num_pages):
    base_url = "https://www.scrapethissite.com/pages/forms/?page={}"
    headers = []
    rows = []

    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"class": "table"})
        if not table:
            print(f"No table found on page {page}")
            continue

        # Extract column headers on first page
        if page == 1:
            headers = [th.get_text(strip=True) for th in table.find_all("th")]

        # Extract rows
        for tr in table.find_all("tr", class_="team"):
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            if cells:
                rows.append(cells)

        delay = random.uniform(1, 5)
        sleep(delay)  # polite delay to avoid overloading server

    # Build DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df

scrape_pages(5)

print(df)