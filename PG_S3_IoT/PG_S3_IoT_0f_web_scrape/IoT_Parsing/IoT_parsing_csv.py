import csv

with open(r'/Users/ramakanthvprabhu/Desktop/PG_S3/PG_S3_IoT/PG_S3_IoT_0f_web_scrape/IoT_Parsing/data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)

    for row in csv_reader:
        row[0] = int(row[0])
        row[1] = float(row[1])
        print(row)